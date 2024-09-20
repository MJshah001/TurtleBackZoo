# Turtleback Zoo Management System

## Project Overview
This project is a database management system built to streamline the operations of Turtleback Zoo, a popular zoo in Livingston, New Jersey. The system was developed as part of a DBMS course project, focusing on the design, implementation, and documentation of a comprehensive zoo management application. The project is built using **Django** and features a relational database designed to manage various zoo assets, daily activities, and generate management reports.

## Features
The system covers three main areas of zoo operations:
1. **Asset Management**: Manages data for animals, employees, buildings, and attractions.
2. **Daily Zoo Activity**: Tracks attendance, ticket sales, and revenue for both attractions and concessions.
3. **Management Reporting**: Provides zoo management with insights into animal care, revenue, and employee performance through various reports.

## Goals of the Project
- Build a database system to manage zoo operations, including animals, employees, and attractions.
- Develop a menu-driven application for zoo employees with easy-to-use interfaces for data entry and management.
- Create a robust reporting system for management to analyze key performance indicators (KPIs) and make informed decisions.

## Key Changes from Phase 1 to Phase 2
- **Concession Handling**: Added concessions as a separate entity for better tracking and reporting.
- **Enclosure Entity**: Created a separate entity for enclosures instead of using attributes in a relationship.
- **Transaction Entity**: Refined the transaction table to handle both animal show and concession transactions.
- **Attraction and Species**: Modified the attraction-requirement-species relationship to an M:N relationship, as animals can participate in multiple shows.

## System Architecture
The system is built with **Django** for the application logic and **PostgreSQL** as the backend database. The following modules are integrated:
- **Animal Management**: Tracks species, health status, and associated personnel (veterinarians and trainers).
- **Attraction Management**: Records show information, including species involved and revenue generated.
- **Employee Management**: Manages different employee types with varying rates and roles within the zoo.
- **Transaction Management**: Handles ticket sales for both zoo attractions and concessions, storing revenue and attendance data.

## Reporting Capabilities
- Daily revenue reports by source (attractions, concessions, and ticket sales).
- Animal population reports, broken down by species, health status, and monthly costs.
- Top attractions based on revenue over customizable date ranges.
- Monthly summaries of the best performing days based on total revenue.

## Challenges Encountered
- **Modeling Transactions**: Integrating animal show and concession transactions into a single schema posed challenges, which we resolved by introducing a specialization approach.
- **Defining Cardinality Constraints**: Determining the relationship between veterinarians, trainers, and species required careful consideration, leading to the decision to assign each specialist to a specific species, while allowing multiple specialists per species.
  
## Future Enhancements
- Expand reporting capabilities for more granular insights.
- Implement a user authentication system for role-based access.
- Develop mobile-friendly interfaces for real-time data entry.

## How to Run the Application
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up the PostgreSQL database and apply migrations: `python manage.py migrate`
4. Run the application: `python manage.py runserver`

