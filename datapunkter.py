TELEMETRY_FIELDS = {
    2: {"name": "meterPvActivePowerAggAvgSiteSingle", "human_text": "Solcelle produktion"},
    3: {"name": "meterGridActivePowerAggAvgSiteSingle", "human_text": "ELnet forbrug"},
    5: {"name": "bmsSocRawArrayCloudTrimmedAggAvgSiteAvg", "human_text": "Batteri status"},
}


def get_telemetry_field_name(human_text):
    for telemetry_field in TELEMETRY_FIELDS.values():
        if telemetry_field['human_text'] == human_text:
            return telemetry_field['name']
    return None


def get_human_text_from_name(name):
    for key, value in TELEMETRY_FIELDS.items():
        if value['name'] == name:
            return value['human_text']
    return None
