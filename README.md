# 🏙️ OneCity Seattle Urban Data Repository

Welcome to a database project where city data meets transparency, organization, and decision-making.

Instead of keeping Seattle-related information scattered across different systems, this project asks:

## ❓ What if Seattle city data could be organized into one centralized database for easier analysis?

The **OneCity Seattle Urban Data Repository** is a DBMS project designed to bring together information about residents, transportation, public services, businesses, complaints, events, tourism, weather, amenities, and housing into one structured relational database.

The goal is to make city-related data easier to store, query, analyze, and understand.


## 📌 What This Project Does

This project designs and implements a relational database system for city-level insights.

It focuses on:

- 🏠 Residents and housing information
- 🚌 Public transportation usage and delays
- 🏢 Business ownership and revenue
- 🏦 Resident bank and spending records
- 🛠️ Public service records
- 📢 Complaint tracking
- 🌦️ Weather conditions
- 🎭 Events and tourism activity
- 🏫 Educational institution mapping
- 🌳 Amenities and community services

The project was built to support both **residents** and **city management** by improving data access, reducing data fragmentation, and enabling better decision-making.


## 📂 Dataset

The database uses city-related data organized into multiple relational tables.

### Main entities include:

- Resident
- Bank
- Business
- Complaint
- Educational Institute
- Residence
- Public Transport
- Public Service
- Amenity
- Event
- Tourist
- Weather

The project also includes relationship tables such as:

- Resident_has_Amenity
- Resident_has_Business
- Resident_has_Transport

These relationships help connect residents with the services, businesses, transportation systems, and amenities they interact with.


## 🛠️ Tech Stack

- **MySQL**
- **SQL**
- **Python**
- **Tkinter**
- **Power BI**
- **ER Modeling**
- **Logical Database Design**
- **Relational Database Management**
- **Data Normalization**
- **SQL Querying**


## 🧠 Methods Used

This project combines database design, SQL development, and basic application building.

### 1. 🏗️ Database Design

The project started with identifying the key city entities and how they relate to each other.

This included designing:

- External model
- Logical model
- Entity relationships
- Primary keys
- Foreign keys
- Relationship tables

The database was structured to make city data easier to query and analyze.


### 2. 🧩 Business Logic Implementation

The project includes real-world rules to make the database more realistic.

Examples of business logic include:

- Only residents can create bank accounts
- Only residents can own businesses
- Only residents can file complaints
- Each resident is connected to one educational institution
- Only residents can own property
- A complaint is linked to a single resident

These rules help keep the database consistent and meaningful.


### 3. 🗃️ Relational Schema Development

The logical model was converted into relational tables using SQL.

The schema includes tables for city entities and their relationships.

This helps organize the data in a way that supports efficient querying and reporting.


### 4. 🔍 SQL Querying

SQL queries were created to answer useful city-level questions, such as:

- Which public transport modes have the highest average delay?
- How many complaints are unresolved?
- Which residents spend more than their income?
- What are the age-group demographics of residents?
- Which amenities have the lowest ratings?
- How does weather relate to transportation delay?
- Which events have the highest attendance?

These queries turn raw database records into useful insights.


### 5. 🖥️ Python Query App

A simple Python interface was created to make the database easier to use.

The app allows users to:

- Select predefined city insight queries
- Run SQL queries
- View results in a table
- Export query results to CSV

This makes the project more interactive and user-friendly.


### 6. 📊 Power BI Dashboard

A dashboard was included to visualize city-level insights.

The dashboard helps present the data in a more accessible way for non-technical users.


## 📊 Results Achieved

This project successfully created a centralized database structure for Seattle city insights.

### Key outcomes:

- Designed a relational database covering multiple city domains
- Created external and logical database models
- Implemented structured tables with relationships between residents, services, transport, businesses, complaints, tourism, events, and weather
- Developed SQL queries for city-level analysis
- Built a Python-based query interface for easier data access
- Added dashboard support for visual reporting
- Organized the project into GitHub-ready folders for SQL, app code, data, documents, and visuals

The final project shows how database design can support better access to city information and help users make sense of complex urban data.


## 🔍 Example Insights Supported by This Database

This database can help answer questions like:

- Which transportation modes experience the most delay?
- Which complaints are still unresolved?
- Which amenities have the lowest ratings?
- Which residents may be financially stressed based on spending and income?
- Which events attract the most residents and tourists?
- How do weather conditions relate to public transportation delays?
- What public services are being used most often?
- Which businesses are owned by younger residents?

These insights can support better planning, resource allocation, and public transparency.


## 🚦 Why This Project Matters

City data is often spread across different systems, making it difficult for residents and decision-makers to get a complete picture.

This project matters because it shows how a centralized database can make city information more organized, accessible, and useful.

For residents, a system like this can improve transparency by helping them understand public services, transportation, complaints, amenities, and community activity.

For city management, it can support better planning by connecting data across different areas of city operations.

In simple terms, this project shows how database systems can help turn scattered city data into structured insights.


## 🎯 Project Goal

The main goal of this project was to design a centralized relational database for Seattle city data.

This project demonstrates:

- Database planning
- ER and logical modeling
- Relational schema design
- SQL query writing
- Data relationships
- Business logic implementation
- Python database connectivity
- Basic user interface development
- Dashboard-based reporting

The project was built to show how DBMS concepts can be used in a realistic city data management scenario.


## 🚀 Future Improvements

This project can be improved in several ways:

- Add stored procedures for common city-management workflows
- Add triggers to enforce rules such as complaint waiting periods and resident-only eligibility
- Build a full web app instead of a Tkinter desktop app
- Add login roles for residents, city officials, and administrators
- Create more Power BI dashboard pages for complaints, transportation, businesses, and public services
- Add more data validation checks before inserting records into the database
- Improve error handling in the Python query app
- Add automated database tests for table relationships and constraints
- Connect the database to real-time or public Seattle open data sources
- Add API endpoints so city data can be accessed by other applications


## 🎯 Note from the Author

I built this project to practice database design using a realistic city-data scenario.

What I liked about this project is that it connects database concepts to a real-world problem: city data is often spread across many systems, and a centralized database can make that information easier to organize, query, and understand.

This project helped me practice relational modeling, SQL queries, business rules, Python database connectivity, and basic dashboard reporting.

In simple terms, the goal was not just to create tables.

The goal was to design a database that could help residents and city decision-makers better understand how a city works.
