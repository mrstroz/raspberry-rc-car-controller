document.addEventListener('DOMContentLoaded', () => {
    const socket = io();
    socket.emit('send_start');

    const stick = document.getElementById('stick');
    const controllerArea = document.getElementById('controllerArea');
    let isDragging = false;

    const controllerRadius = controllerArea.offsetWidth / 2;
    const stickRadius = stick.offsetWidth / 2;
    const centerPoint = {x: controllerRadius, y: controllerRadius};
    let x = 0;
    let y = 0;

    stick.addEventListener('mousedown', () => {
        isDragging = true;
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
        resetStick();
    });

    stick.addEventListener('touchstart', (event) => {
        isDragging = true;
        event.preventDefault();
    });

    document.addEventListener('touchend', () => {
        isDragging = false;
        resetStick();
    });

    document.addEventListener('mousemove', handleMove);
    document.addEventListener('touchmove', handleMove, {passive: false});

    function handleMove(event) {
        if (!isDragging) return;

        const rect = controllerArea.getBoundingClientRect();
        let clientX, clientY;

        if (event.type.startsWith('touch')) {
            clientX = event.touches[0].clientX;
            clientY = event.touches[0].clientY;
        } else {
            clientX = event.clientX;
            clientY = event.clientY;
        }

        x = clientX - rect.left - centerPoint.x;
        y = clientY - rect.top - centerPoint.y;

        const distance = Math.sqrt(x * x + y * y);
        const angle = Math.atan2(y, x);

        const maxDistance = controllerRadius - stickRadius;

        if (distance < maxDistance) {
            stick.style.left = `${centerPoint.x + x}px`;
            stick.style.top = `${centerPoint.y + y}px`;
        } else {
            stick.style.left = `${centerPoint.x + Math.cos(angle) * maxDistance}px`;
            stick.style.top = `${centerPoint.y + Math.sin(angle) * maxDistance}px`;
        }

        let normalizedX = Math.round((x / maxDistance) * 100);
        let normalizedY = Math.round((y / maxDistance) * 100);

        normalizedX > 100 ? normalizedX = 100 : null;
        normalizedX < -100 ? normalizedX = -100 : null;
        normalizedY > 100 ? normalizedY = 100 : null;
        normalizedY < -100 ? normalizedY = -100 : null;

        let speedLeft = -normalizedY - normalizedX;
        let speedRight = -normalizedY + normalizedX;

        speedLeft > 100 ? speedLeft = 100 : null;
        speedLeft < -100 ? speedLeft = -100 : null;
        speedRight > 100 ? speedRight = 100 : null;
        speedRight < -100 ? speedRight = -100 : null;

        emit(speedLeft, speedRight);
    }

    function resetStick() {
        stick.style.left = `${centerPoint.x}px`;
        stick.style.top = `${centerPoint.y}px`;

        emit(0, 0);
        socket.emit('send_reset');
    }

    function emit(speedLeft, speedRight) {
        document.getElementById('speedLeft').innerHTML = speedLeft.toString();
        document.getElementById('speedRight').innerHTML = speedRight.toString();

        console.log(`Left: ${speedLeft}, Right: ${speedRight}`);
        const stickData = {left: speedLeft, right: speedRight};
        socket.emit('send_controller_data', stickData);
    }

});