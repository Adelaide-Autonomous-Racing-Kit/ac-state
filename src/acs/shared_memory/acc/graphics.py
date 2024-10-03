import ctypes

from acs.shared_memory.utils import Point


class GraphicsSharedMemory(ctypes.Structure):
    """
    Enables from buffer copy into an intelligible python object
        each tuple is a (attribute, dtype) pair that presents on
        the resulting object as `graphics_shared_memory.attribute`
    """

    _fields_ = [
        ("packet_id", ctypes.c_int),
        ("acc_status", ctypes.c_int),
        ("acc_session_type", ctypes.c_int),
        ("current_time", ctypes.c_wchar * 15),
        ("last_time", ctypes.c_wchar * 15),
        ("best_time", ctypes.c_wchar * 15),
        ("split", ctypes.c_wchar * 15),
        ("completed_laps", ctypes.c_int),
        ("position", ctypes.c_int),
        ("i_current_time", ctypes.c_int),
        ("i_last_time", ctypes.c_int),
        ("i_best_time", ctypes.c_int),
        ("session_time_left", ctypes.c_float),
        ("distance_traveled", ctypes.c_float),
        ("is_in_pit", ctypes.c_int),
        ("current_sector_index", ctypes.c_int),
        ("last_sector_time", ctypes.c_int),
        ("number_of_laps", ctypes.c_int),
        ("tyre_compound", ctypes.c_wchar * 33),
        ("replay_time_multiplier", ctypes.c_float),
        ("normalised_car_position", ctypes.c_float),
        ("active_cars", ctypes.c_int),
        ("car_coordinates", Point * 60),
        ("car_id", ctypes.c_int * 60),
        ("player_car_id", ctypes.c_int),
        ("penalty_time", ctypes.c_float),
        ("flag", ctypes.c_int),
        ("penalty", ctypes.c_int),
        ("ideal_line_on", ctypes.c_int),
        ("is_in_pit_lane", ctypes.c_int),
        ("surface_grip", ctypes.c_float),
        ("mandatory_pit_done", ctypes.c_int),
        ("wind_speed", ctypes.c_float),
        ("wind_direction", ctypes.c_float),
        ("is_setup_menu_visible", ctypes.c_int),
        ("main_display_index", ctypes.c_int),
        ("secondary_disply_index", ctypes.c_int),
        ("traction_control", ctypes.c_int),
        ("traction_control_cut", ctypes.c_int),
        ("engine_map", ctypes.c_int),
        ("anti_lock_braking_system", ctypes.c_int),
        ("fuel_x_lap", ctypes.c_float),
        ("rain_lights", ctypes.c_int),
        ("flashing_lights", ctypes.c_int),
        ("light_stage", ctypes.c_int),
        ("exhaust_temperature", ctypes.c_float),
        ("wiper_stage", ctypes.c_int),
        ("driver_stint_total_time_remaining", ctypes.c_int),
        ("driver_stint_time_remaining", ctypes.c_int),
        ("rain_tyres", ctypes.c_int),
        ("session_index", ctypes.c_int),
        ("used_fuel", ctypes.c_float),
        ("delta_laptime", ctypes.c_wchar * 15),
        ("i_delta_laptime", ctypes.c_int),
        ("estimated_laptime", ctypes.c_wchar * 15),
        ("i_estimated_laptime", ctypes.c_int),
        ("is_delta_positive", ctypes.c_int),
        ("i_split", ctypes.c_int),
        ("is_valid_lap", ctypes.c_int),
        ("fuel_estimated_laps", ctypes.c_float),
        ("track_status", ctypes.c_wchar * 33),
        ("missing_mandatory_pits", ctypes.c_int),
        ("clock", ctypes.c_float),
        ("direction_lights_left", ctypes.c_int),
        ("direction_lights_right", ctypes.c_int),
        ("global_yellow", ctypes.c_int),
        ("global_yellow_1", ctypes.c_int),
        ("global_yellow_2", ctypes.c_int),
        ("global_yellow_3", ctypes.c_int),
        ("global_white", ctypes.c_int),
        ("global_green", ctypes.c_int),
        ("global_chequered", ctypes.c_int),
        ("global_red", ctypes.c_int),
        ("mfd_tyre_set", ctypes.c_int),
        ("mfd_fuel_to_add", ctypes.c_float),
        ("mfd_tyre_pressure_FL", ctypes.c_float),
        ("mfd_tyre_pressure_FR", ctypes.c_float),
        ("mfd_tyre_pressure_RL", ctypes.c_float),
        ("mfd_tyre_pressure_RR", ctypes.c_float),
        ("track_grip_status", ctypes.c_int),
        ("rain_intensity", ctypes.c_int),
        ("rain_intensity_in_10_minutes", ctypes.c_int),
        ("rain_intensity_in_30_minutes", ctypes.c_int),
        ("current_tyre_set", ctypes.c_int),
        ("strategy_tyre_set", ctypes.c_int),
        ("gap_ahead", ctypes.c_int),
        ("gap_behind", ctypes.c_int),
    ]

    dtypes = [
        ("packet_id", ctypes.c_int),
        ("acc_status", ctypes.c_int),
        ("acc_session_type", ctypes.c_int),
        ("current_time", "V30"),
        ("last_time", "V30"),
        ("best_time", "V30"),
        ("split", "V30"),
        ("completed_laps", ctypes.c_int),
        ("position", ctypes.c_int),
        ("i_current_time", ctypes.c_int),
        ("i_last_time", ctypes.c_int),
        ("i_best_time", ctypes.c_int),
        ("session_time_left", ctypes.c_float),
        ("distance_traveled", ctypes.c_float),
        ("is_in_pit", ctypes.c_int),
        ("current_sector_index", ctypes.c_int),
        ("last_sector_time", ctypes.c_int),
        ("number_of_laps", ctypes.c_int),
        ("tyre_compound", "V68"),
        ("replay_time_multiplier", ctypes.c_float),
        ("normalised_car_position", ctypes.c_float),
        ("active_cars", ctypes.c_int),
        ("car_coordinates", Point * 60),
        ("car_id", ctypes.c_int * 60),
        ("player_car_id", ctypes.c_int),
        ("penalty_time", ctypes.c_float),
        ("flag", ctypes.c_int),
        ("penalty", ctypes.c_int),
        ("ideal_line_on", ctypes.c_int),
        ("is_in_pit_lane", ctypes.c_int),
        ("surface_grip", ctypes.c_float),
        ("mandatory_pit_done", ctypes.c_int),
        ("wind_speed", ctypes.c_float),
        ("wind_direction", ctypes.c_float),
        ("is_setup_menu_visible", ctypes.c_int),
        ("main_display_index", ctypes.c_int),
        ("secondary_disply_index", ctypes.c_int),
        ("traction_control", ctypes.c_int),
        ("traction_control_cut", ctypes.c_int),
        ("engine_map", ctypes.c_int),
        ("anti_lock_braking_system", ctypes.c_int),
        ("fuel_x_lap", ctypes.c_float),
        ("rain_lights", ctypes.c_int),
        ("flashing_lights", ctypes.c_int),
        ("light_stage", ctypes.c_int),
        ("exhaust_temperature", ctypes.c_float),
        ("wiper_stage", ctypes.c_int),
        ("driver_stint_total_time_remaining", ctypes.c_int),
        ("driver_stint_time_remaining", ctypes.c_int),
        ("rain_tyres", ctypes.c_int),
        ("session_index", ctypes.c_int),
        ("used_fuel", ctypes.c_float),
        ("delta_laptime", "V32"),
        ("i_delta_laptime", ctypes.c_int),
        ("estimated_laptime", "V32"),
        ("i_estimated_laptime", ctypes.c_int),
        ("is_delta_positive", ctypes.c_int),
        ("i_split", ctypes.c_int),
        ("is_valid_lap", ctypes.c_int),
        ("fuel_estimated_laps", ctypes.c_float),
        ("track_status", "V68"),
        ("missing_mandatory_pits", ctypes.c_int),
        ("clock", ctypes.c_float),
        ("direction_lights_left", ctypes.c_int),
        ("direction_lights_right", ctypes.c_int),
        ("global_yellow", ctypes.c_int),
        ("global_yellow_1", ctypes.c_int),
        ("global_yellow_2", ctypes.c_int),
        ("global_yellow_3", ctypes.c_int),
        ("global_white", ctypes.c_int),
        ("global_green", ctypes.c_int),
        ("global_chequered", ctypes.c_int),
        ("global_red", ctypes.c_int),
        ("mfd_tyre_set", ctypes.c_int),
        ("mfd_fuel_to_add", ctypes.c_float),
        ("mfd_tyre_pressure_FL", ctypes.c_float),
        ("mfd_tyre_pressure_FR", ctypes.c_float),
        ("mfd_tyre_pressure_RL", ctypes.c_float),
        ("mfd_tyre_pressure_RR", ctypes.c_float),
        ("track_grip_status", ctypes.c_int),
        ("rain_intensity", ctypes.c_int),
        ("rain_intensity_in_10_minutes", ctypes.c_int),
        ("rain_intensity_in_30_minutes", ctypes.c_int),
        ("current_tyre_set", ctypes.c_int),
        ("strategy_tyre_set", ctypes.c_int),
        ("gap_ahead", ctypes.c_int),
        ("gap_behind", ctypes.c_int),
    ]