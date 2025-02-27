# CS-340-MongoDB
CS 340 MongoDB Projects
# CS 340 Project Portfolio

## Overview
This repository contains the code and documentation for **Project Two** of CS 340, which includes the final dashboard and the associated code from **Project One**. In **Project One**, I created a CRUD Python module to handle database operations, which was then integrated into the dashboard in **Project Two**. The dashboard allows users to interact with the data and visualize key business metrics dynamically.

## Project Files
- **Project One (CRUD Python Module)**: Handles database operations—Create, Read, Update, and Delete (CRUD)—for the dashboard.
- **Project Two (Dashboard)**: Implements the dashboard connected to the database and allows dynamic interaction and visualization.
- **README**: This file, containing information about the project and the questions answered below.

## How to Use
1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the Python scripts to set up and interact with the dashboard.

## Reflection Questions

### How do you write programs that are maintainable, readable, and adaptable?
To ensure programs are maintainable, readable, and adaptable, I follow principles such as modularization, clear commenting, and adhering to coding standards. For example, in **Project One**, I created a **CRUD Python module** to handle the database operations. By encapsulating the **Create**, **Read**, **Update**, and **Delete** operations into a single module, I made it easier to reuse across different parts of the dashboard in **Project Two**. This approach enhanced maintainability, as any changes to the database logic (like modifying queries or adding new operations) could be made in one place, reducing code duplication.

The advantage of working this way was that it made the dashboard widgets adaptable to changes in the database without needing extensive rework. If the database schema changes, I can quickly modify the CRUD module and not affect other parts of the application. This modularity also makes it easier for others to maintain and scale the system.

In the future, I could use this **CRUD Python module** in any project that requires database interaction, whether it’s for another dashboard, an application, or even a REST API, as it would streamline the process of managing data with minimal changes to the codebase.

### How do you approach a problem as a computer scientist?
As a computer scientist, I approach problems by first understanding the requirements and breaking down the problem into smaller, manageable tasks. For the **Grazioso Salvare** project, the task was to create a dashboard that could connect to a database and visualize data. My first step was to analyze the data structure and understand what information the client needed to visualize, ensuring that the database schema was suitable for those needs.

In this project, my approach was more structured and client-focused. Unlike in previous assignments where I might have worked with more abstract requirements, here I had to ensure that the system directly served the client’s business goals—namely, allowing the dashboard to display relevant data dynamically and interactively. I focused on building the database and dashboard with scalability in mind, ensuring that it could be adapted for future use cases.

In future projects, I would continue to take a **client-centered approach** and focus on understanding their specific needs. I would employ techniques like **normalization** for database design to ensure the structure is efficient, and I would use **Agile methodologies** for iterative development and feedback. This approach would help to ensure that the database meets both current and potential future requirements.

### What do computer scientists do, and why does it matter?
Computer scientists design and build systems that solve real-world problems through the application of algorithms, data structures, and programming languages. They create software and applications that streamline processes, automate tasks, and make data-driven decisions easier and faster.

In the case of **Grazioso Salvare**, the work I did on the dashboard and the database would help the company make better decisions by providing them with easy-to-use tools for analyzing and visualizing business-critical data. The dashboard allows them to track **key performance indicators (KPIs)** in real-time, reducing the manual effort required to gather and analyze data. This would enable better decision-making, faster response times, and a more informed understanding of their operations.

The importance of computer science lies in its ability to turn complex problems into manageable solutions, and this project is a perfect example of how technology can directly improve the effectiveness and efficiency of a business. By automating data processing and visualization, the company can focus on growing their business instead of spending time managing and analyzing data manually.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Professor [Instructor Name] for their guidance throughout this course.
- [Any other contributors or resources that helped you in this project].

