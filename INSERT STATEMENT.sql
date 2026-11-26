USE BigData4;
GO

-- 1. Insert parent COLLISION record (Satisfies COLLISION foreign key)
INSERT INTO COLLISION (collision_index, collision_year, collision_ref_no)
VALUES ('2023010000001', 2023, 'REF-2023-001');
GO

-- 2. Insert geographic reference record (Satisfies LSOA_REFERENCE foreign key)
INSERT INTO LSOA_REFERENCE (lsoa_of_casualty, casualty_imd_decile)
VALUES ('E01028532', 3);
GO

-- 3. Insert parent VEHICLE record (Satisfies composite VEHICLE foreign key)
INSERT INTO VEHICLE (collision_index, vehicle_reference)
VALUES ('2023010000001', 1);
GO

-- 4. Insert the new CASUALTY record including all relevant attributes
INSERT INTO CASUALTY (
    collision_index,
    vehicle_reference,
    casualty_reference,
    lsoa_of_casualty,
    casualty_class,
    sex_of_casualty,
    age_of_casualty,
    age_band_of_casualty,
    casualty_severity,
    pedestrian_location,
    pedestrian_movement,
    car_passenger,
    bus_or_coach_passenger,
    pedestrian_road_maintenance_worker,
    casualty_type,
    enhanced_casualty_severity,
    casualty_injury_based,
    casualty_adjusted_severity_serious,
    casualty_adjusted_severity_slight,
    casualty_distance_banding
)
VALUES (
    '2023010000001',                   -- collision_index (Foreign Key)
    1,                                  -- vehicle_reference (Composite Foreign Key)
    1,                                  -- casualty_reference (Primary Key component)
    'E01028532',                        -- lsoa_of_casualty (Foreign Key to LSOA_REFERENCE)
    'Pedestrian',                       -- casualty_class
    'Male',                             -- sex_of_casualty
    34,                                 -- age_of_casualty
    '31-35',                            -- age_band_of_casualty
    'Serious',                          -- casualty_severity
    1,                                  -- pedestrian_location
    2,                                  -- pedestrian_movement
    NULL,                               -- car_passenger
    NULL,                               -- bus_or_coach_passenger
    0,                                  -- pedestrian_road_maintenance_worker
    'Pedestrian',                       -- casualty_type
    'Serious Injury',                   -- enhanced_casualty_severity
    'Fracture',                         -- casualty_injury_based
    0.85,                               -- casualty_adjusted_severity_serious
    0.15,                               -- casualty_adjusted_severity_slight
    '0 - 5 miles'                       -- casualty_distance_banding
);
GO