function contactMessage() {
    alert("Welcome to Larbod. We will contact you soon!");
}
const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();
    const formMessage = document.getElementById("formMessage");

    if (name === "" || email === "" || message === "") {
        formMessage.textContent = "Please fill in all fields.";
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
