-- Create the new database
CREATE DATABASE BigData4;

-- 1. COLLISION Table (Parent)
CREATE TABLE COLLISION (
    collision_index VARCHAR(20) PRIMARY KEY,
    collision_year INT NULL,
    collision_ref_no VARCHAR(50) NULL
);
GO

-- 2. LSOA_REFERENCE Table (Geographic Lookup)
CREATE TABLE LSOA_REFERENCE (
    lsoa_of_casualty VARCHAR(20) PRIMARY KEY,
    casualty_imd_decile INT NULL
);
GO

-- 3. VEHICLE Table (Child of Collision)
CREATE TABLE VEHICLE (
    collision_index VARCHAR(20) NOT NULL,
    vehicle_reference INT NOT NULL,
    PRIMARY KEY (collision_index, vehicle_reference),
    FOREIGN KEY (collision_index) REFERENCES COLLISION(collision_index)
);
GO

-- 4. CASUALTY Table (Child of Vehicle, references LSOA_REFERENCE)
CREATE TABLE CASUALTY (
    collision_index VARCHAR(20) NOT NULL,
    vehicle_reference INT NOT NULL,
    casualty_reference INT NOT NULL,
    lsoa_of_casualty VARCHAR(20) NULL,
    casualty_class VARCHAR(50) NULL,
    sex_of_casualty VARCHAR(20) NULL,
    age_of_casualty INT NULL,
    age_band_of_casualty VARCHAR(50) NULL,
    casualty_severity VARCHAR(50) NULL,
    pedestrian_location INT NULL,
    pedestrian_movement INT NULL,
    car_passenger INT NULL,
    bus_or_coach_passenger INT NULL,
    pedestrian_road_maintenance_worker INT NULL,
    casualty_type VARCHAR(50) NULL,
    enhanced_casualty_severity VARCHAR(50) NULL,
    casualty_injury_based VARCHAR(50) NULL,
    casualty_adjusted_severity_serious FLOAT NULL,
    casualty_adjusted_severity_slight FLOAT NULL,
    casualty_distance_banding VARCHAR(50) NULL,
    PRIMARY KEY (collision_index, vehicle_reference, casualty_reference),
    FOREIGN KEY (collision_index, vehicle_reference) REFERENCES VEHICLE(collision_index, vehicle_reference),
    FOREIGN KEY (lsoa_of_casualty) REFERENCES LSOA_REFERENCE(lsoa_of_casualty)
);
GO