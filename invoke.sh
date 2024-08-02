curl -X POST http://0.0.0.0:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"Type": 2, "Air_temperature": 297.2, "Process_temperature": 308.2, "Rotational_speed": 3678.3, "Torque_NM": 8.1, "Tool_wear_min": 133.3}'