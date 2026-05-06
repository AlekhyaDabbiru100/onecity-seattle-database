QUERIES = {
    "1. Monthly Avg Temperature & Humidity": """
        SELECT 
            DATE_FORMAT(w.Date_ID, '%Y-%m') AS Month,
            AVG(w.Temp) AS Avg_Temperature,
            AVG(w.Humidity) AS Avg_Humidity
        FROM Weather w
        GROUP BY DATE_FORMAT(w.Date_ID, '%Y-%m')
        ORDER BY Month;
    """,

    "2. Average Transport Delay": """
        SELECT 
            pt.`Transport Mode`,
            AVG(pt.`Delay Time`) AS Avg_Delay_Time
        FROM Public_Transport pt
        GROUP BY pt.`Transport Mode`;
    """,

    "3. Unresolved Complaints Count": """
        SELECT 
            Status,
            COUNT(*) AS Complaint_Count
        FROM Complaint
        WHERE Status IN ('Pending', 'In Progress')
        GROUP BY Status;
    """,

    "4. Residents Spending More Than Income": """
        SELECT 
            r.Resident_ID,
            r.First_Name,
            r.Last_Name,
            SUM(b.Outflow) AS Total_Spent,
            SUM(b.Inflow) AS Total_Income
        FROM Resident r
        JOIN Bank b 
            ON r.Resident_ID = b.Resident_Resident_ID
        GROUP BY 
            r.Resident_ID,
            r.First_Name,
            r.Last_Name
        HAVING SUM(b.Outflow) > SUM(b.Inflow);
    """,

    "5. Age Group Demographics of Residents": """
        SELECT
            CASE
                WHEN TIMESTAMPDIFF(YEAR, r.DoB, CURDATE()) < 18 THEN 'Child'
                WHEN TIMESTAMPDIFF(YEAR, r.DoB, CURDATE()) BETWEEN 18 AND 55 THEN 'Adult'
                ELSE 'Senior'
            END AS Age_Group,
            COUNT(*) AS Total_Residents
        FROM Resident r
        GROUP BY Age_Group
        ORDER BY Total_Residents DESC;
    """,

    "6. Lowest-Rated Amenities": """
        SELECT 
            a.Type AS Amenity_Type,
            MIN(a.Rating) AS Lowest_Rating
        FROM Amenity a
        GROUP BY a.Type
        ORDER BY Lowest_Rating ASC
        LIMIT 10;
    """,

    "7. Average Transport Delay per Resident": """
        SELECT 
            r.Resident_ID,
            r.First_Name,
            r.Last_Name,
            AVG(pt.`Delay Time`) AS Avg_Transport_Delay
        FROM Resident r
        JOIN Resident_has_Transport rht 
            ON r.Resident_ID = rht.Resident_Resident_ID
        JOIN Public_Transport pt 
            ON rht.Transport_Vehicle_ID = pt.Vehicle_ID
        GROUP BY 
            r.Resident_ID,
            r.First_Name,
            r.Last_Name;
    """,

    "8. Top 10 Businesses by Young Entrepreneurs": """
        SELECT 
            b.Business_ID,
            b.Type AS Business_Type,
            AVG(b.Revenue) AS Avg_Revenue
        FROM Business b
        JOIN Resident_has_Business rhb 
            ON b.Business_ID = rhb.Business_Business_ID
        JOIN Resident r 
            ON rhb.Resident_Resident_ID = r.Resident_ID
        WHERE TIMESTAMPDIFF(YEAR, r.DoB, CURDATE()) BETWEEN 18 AND 30
        GROUP BY 
            b.Business_ID,
            b.Type
        ORDER BY Avg_Revenue DESC
        LIMIT 10;
    """,

    "9. Weather vs Transport Delay": """
        SELECT 
            w.Date_ID,
            COALESCE(w.Temp, 0) AS Temp,
            COALESCE(w.Humidity, 0) AS Humidity,
            COALESCE(w.AQI, 0) AS AQI,
            COUNT(pt.Vehicle_ID) AS Total_Trips,
            AVG(pt.`Delay Time`) AS Avg_Delay
        FROM Weather w
        JOIN Public_Transport pt 
            ON w.Date_ID = pt.Date
        GROUP BY 
            w.Date_ID,
            w.Temp,
            w.Humidity,
            w.AQI
        ORDER BY Avg_Delay DESC;
    """,

    "10. Event Participation Insights": """
        SELECT 
            e.Event_ID,
            e.Type,
            e.Location,
            COUNT(DISTINCT r.Resident_ID) AS Resident_Attendance,
            COUNT(DISTINCT t.`Tourist ID`) AS Tourist_Attendance,
            (
                COUNT(DISTINCT r.Resident_ID) + 
                COUNT(DISTINCT t.`Tourist ID`)
            ) AS Total_Attendance
        FROM Event e
        LEFT JOIN Resident r 
            ON e.Event_ID = r.Event_Event_ID
        LEFT JOIN Tourist t 
            ON e.Event_ID = t.`Event_Event ID`
        GROUP BY 
            e.Event_ID,
            e.Type,
            e.Location
        ORDER BY Total_Attendance DESC;
    """,

    "11. Tourists Attending Events": """
        SELECT 
            t.`First Name`,
            t.`Last Name`,
            e.Type AS Event_Type,
            t.`Duration of Stay`
        FROM Tourist t
        JOIN Event e 
            ON t.`Event_Event ID` = e.Event_ID
        WHERE t.IsAttendingEvent = 1;
    """,

    "12. Recent Complaints and Public Services": """
        SELECT 
            Complaint_ID AS Record_ID,
            Description AS Detail,
            Date AS Record_Date,
            'Complaint' AS Record_Type
        FROM Complaint
        WHERE Date BETWEEN DATE_SUB(CURDATE(), INTERVAL 730 DAY) AND CURDATE()

        UNION ALL

        SELECT 
            Public_Service_ID AS Record_ID,
            CONCAT(First_Name, ' ', Last_Name) AS Detail,
            DATE(Date_time) AS Record_Date,
            'Public_Service' AS Record_Type
        FROM Public_Service
        WHERE Date_time >= DATE_SUB(CURDATE(), INTERVAL 730 DAY);
    """
}