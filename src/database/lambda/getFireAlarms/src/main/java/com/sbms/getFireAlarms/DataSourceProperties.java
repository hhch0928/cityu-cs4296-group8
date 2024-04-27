package com.sbms.getFireAlarms;

public class DataSourceProperties {

    private final String host;
    private final int port;
    private final String db;
    private final String username;
    private final String password;

    public DataSourceProperties() {
        this.host = System.getenv("RDS_HOSTNAME");
        this.db = System.getenv("RDS_DB_NAME");
        this.username = System.getenv("RDS_USERNAME");
        this.password = System.getenv("RDS_PASSWORD");
        this.port = Integer.parseInt(System.getenv("RDS_PORT"));
    }

    public DataSourceProperties(String host, int port, String db, String username, String password) {
        this.host = host;
        this.port = port;
        this.db = db;
        this.username = username;
        this.password = password;
    }

    public String getHost() {
        return host;
    }

    public int getPort() {
        return port;
    }

    public String getDb() {
        return db;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    @Override
    public String toString() {
        return "DataSourceProperties{" +
                "host='" + host + '\'' +
                ", port=" + port +
                ", db='" + db + '\'' +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }

}
