package com.sbms.getFireAlarms;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ListFireAlarmsTest {

    private ListFireAlarms fireAlarms;
    private DataSourceProperties db;

    @BeforeEach
    void setup() {
        db = new DataSourceProperties("sbms.c3880y8iqvuo.us-east-1.rds.amazonaws.com",5432,"sbms","postgres","password");
        fireAlarms = new ListFireAlarms(db);
    }

    @Test
    void shouldListAllFireAlarms() {
        List<String> alarms = fireAlarms.handleRequest();
        for (String alarm: alarms) {
            System.out.println(alarm);
        }
        assertEquals(40, alarms.size());
    }

}
