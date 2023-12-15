document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

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

    document.addEventListener('mousemove', (event) => {
        if (!isDragging) return;

        const rect = controllerArea.getBoundingClientRect();
        console.log(rect);
        x = event.clientX - rect.left - centerPoint.x;
        y = event.clientY - rect.top - centerPoint.y;

        const distance = Math.sqrt(x * x + y * y);
        const angle = Math.atan2(y, x);

        if (distance < controllerRadius - stickRadius) {
            stick.style.left = `${centerPoint.x + x}px`;
            stick.style.top = `${centerPoint.y + y}px`;
        } else {
            stick.style.left = `${centerPoint.x + Math.cos(angle) * (controllerRadius - stickRadius)}px`;
            stick.style.top = `${centerPoint.y + Math.sin(angle) * (controllerRadius - stickRadius)}px`;
        }

        console.log(`X: ${x}, Y: ${y}`);
        const stickData = {x: x, y: y};
        socket.emit('send_controller_data', stickData);
    });

    function resetStick() {
        stick.style.left = `${centerPoint.x}px`;
        stick.style.top = `${centerPoint.y}px`;
        x = 0;
        y = 0;
        console.log(`X: ${x}, Y: ${y}`);
        const stickData = {x: x, y: y};
        socket.emit('send_stick_data', stickData);
    }

});