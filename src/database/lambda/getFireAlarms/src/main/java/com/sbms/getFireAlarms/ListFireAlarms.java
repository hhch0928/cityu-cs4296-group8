package com.sbms.getFireAlarms;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ListFireAlarms {

    private List<String> firealarms = new ArrayList<>();

    private final DataSourceProperties db;

    public ListFireAlarms() {
        this.db = new DataSourceProperties();
    }

    public ListFireAlarms(DataSourceProperties db) {
        this.db = db;
    }

    public List<String> handleRequest() {
        String jdbcURL = "jdbc:postgresql://sbms.c3880y8iqvuo.us-east-1.rds.amazonaws.com:5432/sbms";

        try(Connection conn = DriverManager.getConnection(jdbcURL, "postgres", "password")) {
            if(!conn.isValid(0)) {
                System.out.println("Unable to connect to: " + jdbcURL);
                System.exit(0);
            }
            PreparedStatement selectStatement = conn.prepareStatement("SELECT * FROM fire_alarm");
            ResultSet rs = selectStatement.executeQuery();
            while(rs.next()) {
                // Assuming you want to format the data as a JSON string
                String alarmData = String.format(
                        "{\"fire_alarmid\": %d, \"alarm_end_tm\": \"%s\", \"alarm_start_tm\": \"%s\", " +
                                "\"description\": \"%s\", \"fire_alarm_status\": \"%s\", \"heat_level\": %f, " +
                                "\"location_id\": %d, \"public_address\": %b, \"smoke_level\": %f}",
                        rs.getInt("fire_alarmid"),
                        rs.getTimestamp("alarm_end_tm"),
                        rs.getTimestamp("alarm_start_tm"),
                        rs.getString("description"),
                        rs.getString("fire_alarm_status"),
                        rs.getDouble("heat_level"),
                        rs.getInt("location_id"),
                        rs.getBoolean("public_address"),
                        rs.getDouble("smoke_level")
                );
                firealarms.add(alarmData);
            }
        } catch (SQLException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }

        return firealarms;
    }
}
