function contactMessage() {
    alert("Welcome to Larbod. We will contact you soon!");
}
const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const budget = document.getElementById("budget").value;
    const projectType = document.getElementById("projectType").value;
    const message = document.getElementById("message").value.trim();
    const formMessage = document.getElementById("formMessage");

    if (
    name === "" ||
    email === "" ||
    budget === "" ||
    projectType === "" ||
    message === ""
) {
    formMessage.textContent = "Please complete all project details.";
    formMessage.className = "error";
    return;
}

    formMessage.textContent = "Thank you! Your message is ready to be sent.";
    formMessage.className = "success";

    contactForm.reset();
});
function viewProject(project) {
    const title = document.getElementById("projectTitle");
    const description = document.getElementById("projectDescription");

    if (project === "website") {
        title.textContent = "Business Website";
        description.textContent =
            "A modern responsive website built to help a business attract customers and present its services professionally.";
    }

    if (project === "automation") {
        title.textContent = "Automation System";
        description.textContent =
            "A workflow designed to reduce repetitive tasks and improve business efficiency.";
    }

    if (project === "api") {
        title.textContent = "API Integration";
        description.textContent =
            "A system that connects different applications so they can exchange data automatically.";
    }
    document.getElementById("projectDetails").scrollIntoView({
    behavior: "smooth"
});
}
function selectService(service) {
    const projectType = document.getElementById("projectType");
    const message = document.getElementById("message");

    const serviceValues = {
        "Website Development": "website",
        "Automation": "automation",
        "API Development": "api",
        "AI Solutions": "ai"
    };

    projectType.value = serviceValues[service];

    message.value = "I am interested in: " + service;

    document.getElementById("contact").scrollIntoView({
        behavior: "smooth"
    });
}