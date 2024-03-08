from enum import Enum


class DemoSite(Enum):
    BERLIN = "Berlin-Brandenburg, DE"
    CATALONIA = "Coast of Catalonia, ES"
    ATTICA = "Region of Attica, GR"
    ZEELAND = "Province of Zeeland, NL"
    TROMS = "Troms & Finnmark, NO"
    ZEMGALE = "Zemgale region, LV"
    LAGHI = "Valle dei Laghi area, IT"
    NONE = "Not specified"


class AssessmentType(Enum):
    QUALITATIVE = "qualitative"
    QUANTITATIVE_REFERENCE = "quantitative-reference"
    QUANTITATIVE_MIN_MAX = "quantitative-min-max"


class StakeHolderType(Enum):
    Public = "Public"
    Private = "Private"
    Academic = "Academic"
    Government = "Government"
    Ngo = "NGO"
    NONE = "Not Specified"
