function contactMessage() {
    alert("Welcome to Larbod. We will contact you soon!");
}
const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", async function(event) {
    console.log("Form submitted");
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const budget = document.getElementById("budget").value;
    const projectType = document.getElementById("projectType").value;
    const message = document.getElementById("message").value.trim();
    const formMessage = document.getElementById("formMessage");
    const submitButton = document.getElementById("submitButton");

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

    submitButton.disabled = true;
    submitButton.textContent = "Sending...";

    try {
        const response = await fetch("/contact", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: name,
                email: email,
                budget: budget,
                project_type: projectType,
                message: message
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || "Message could not be sent"
            );
        }

        formMessage.textContent = "Message sent successfully!";
        formMessage.className = "success";

        contactForm.reset();

    } catch (error) {
        console.error(error);

        formMessage.textContent =
            "Something went wrong. Please try again.";

        formMessage.className = "error";

    } finally {
        submitButton.disabled = false;
        submitButton.textContent = "Send Message";
    }
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