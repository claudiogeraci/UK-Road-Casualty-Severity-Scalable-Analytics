USE BigData4;
GO

SELECT 
    c.collision_index,
    c.collision_year,
    c.collision_ref_no,
    v.vehicle_reference,
    cs.casualty_reference,
    cs.casualty_severity,
    cs.casualty_class,
    cs.casualty_type,
    cs.age_of_casualty,
    lr.casualty_imd_decile
FROM CASUALTY cs
INNER JOIN VEHICLE v 
    ON cs.collision_index = v.collision_index 
    AND cs.vehicle_reference = v.vehicle_reference
INNER JOIN COLLISION c 
    ON cs.collision_index = c.collision_index
LEFT JOIN LSOA_REFERENCE lr 
    ON cs.lsoa_of_casualty = lr.lsoa_of_casualty
WHERE cs.casualty_severity IN ('Fatal', 'Serious')
  AND (cs.casualty_class = 'Pedestrian' OR cs.casualty_type = 'Pedestrian')
  AND c.collision_year = 2023; -- Specific condition example (e.g., specific year or filter criteria)
GO