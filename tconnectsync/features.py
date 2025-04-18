import os
from dotenv import load_dotenv
from .secret import ENABLE_TESTING_MODES

load_dotenv()

"""Supported synchronization features."""
BASAL = "BASAL"
BOLUS = "BOLUS"
IOB = "IOB"
BOLUS_BG = "BOLUS_BG"
CGM = "CGM"
PUMP_EVENTS = "PUMP_EVENTS"
PUMP_EVENTS_BASAL_SUSPENSION = "PUMP_EVENTS_BASAL_SUSPENSION"
PROFILES = "PROFILES"
CGM_ALERTS = "CGM_ALERTS"
DEVICE_STATUS = "DEVICE_STATUS"

DEFAULT_FEATURES = [
    BASAL,
    BOLUS,
    PUMP_EVENTS,
    PROFILES
]

ALL_FEATURES = [
    BASAL,
    BOLUS,
    IOB,
    PUMP_EVENTS,
    PUMP_EVENTS_BASAL_SUSPENSION,
    PROFILES,
    CGM,
    CGM_ALERTS,
    DEVICE_STATUS,
]

if ENABLE_TESTING_MODES:
    ALL_FEATURES += [BOLUS_BG]

# Aliases from .env to internal constants
ALIASES = {
    "INSULIN": IOB,
    "CARBS": CGM,
    "SET_CHANGE": DEVICE_STATUS,
    "CANNULA_CHANGE": DEVICE_STATUS,
    "CARTRIDGE_CHANGE": DEVICE_STATUS,
    "STATUS": DEVICE_STATUS,
}

env_features = os.getenv("FEATURES")

if env_features:
    raw_list = [f.strip().upper() for f in env_features.split(",") if f.strip()]
    ENABLED_FEATURES = list({
        ALIASES.get(f, f) for f in raw_list if ALIASES.get(f, f) in ALL_FEATURES
    })
else:
    ENABLED_FEATURES = DEFAULT_FEATURES.copy()

if ENABLE_TESTING_MODES and BOLUS_BG not in ENABLED_FEATURES:
    ENABLED_FEATURES.append(BOLUS_BG)

# Debug log to confirm what we’re loading
print(f"🔧 FINAL ENABLED FEATURES: {ENABLED_FEATURES}")
