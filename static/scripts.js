let currentStep = 1;
const totalSteps = 3; // Adjust based on the number of steps

function showStep(step) {
    $('.step').hide();
    $(`#step-${step}`).show();
}

function nextStep() {
    if (currentStep < totalSteps) {
        currentStep++;
        showStep(currentStep);
    }
}

function prevStep() {
    if (currentStep > 1) {
        currentStep--;
        showStep(currentStep);
    }
}

$(document).ready(function() {
    showStep(currentStep);
});
