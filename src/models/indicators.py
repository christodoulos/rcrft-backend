from src.const import *
from src.enums import AssessmentType
import mongoengine as me
from typing import List

class CodeAndDescription(me.EmbeddedDocument):
    code = me.StringField()
    description = me.StringField()


class Assessment(me.EmbeddedDocument):
    user = me.StringField(required=True)
    assessment_type = me.EnumField(AssessmentType, required=True)
    value = me.FloatField(default=NEG_INT)
    reference_value = me.FloatField(default=NEG_INT)
    min_value = me.FloatField(default=NEG_INT)
    max_value = me.FloatField(default=NEG_INT)
    is_inverse = me.BooleanField(default=False)
    alternative_description = me.StringField(default=EMPTY_STR)
    normalized_value = me.FloatField(required=True)
    degree_of_certainty = me.FloatField(required=True)
    indicator_weight = me.FloatField(required=True)


class Indicator(me.Document):
    meta = {"collection": "indicators", "db_alias": "rcrft"}

    definedBy = me.StringField(required=True, default="IMPETUS")
    category = me.EmbeddedDocumentField(CodeAndDescription)
    subcategory = me.EmbeddedDocumentField(CodeAndDescription)
    code = me.StringField()
    description = me.StringField(unique=True)
    principal = me.StringField()
    main_climate_change_factor = me.StringField()
    other_climate_change_factors = me.StringField()
    main_affected_sector = me.StringField()
    other_affected_sectors = me.StringField()
    type = me.StringField()
    metrics_and_units = me.StringField()
    spatial_scale = me.StringField()
    data_requirements = me.StringField(default="")
    references = me.StringField()
    typology = me.StringField()
    kind = me.StringField(choices=["vulnerability", "adaptation", "resilience"])
    assessments = me.EmbeddedDocumentListField(Assessment)
    
    
    @staticmethod
    def get_by_description(description: str) -> "Indicator":
        return Indicator.objects(description=description).first()


    @staticmethod
    def get_all_assessments() -> List[Assessment]:
        return Indicator.objects().values_list("assessments")
    

    @staticmethod
    def get_all_indicators() -> List["Indicator"]:
        return Indicator.objects()


    @staticmethod
    def clear_all_assessments() -> None:
        all_indicators = Indicator.get_all_indicators()
        for indicator in all_indicators:
            # indicator.assessments = [Assessment(assessment_type=AssessmentType.QUALITATIVE, user=EMPTY_STR, normalized_value=NEG_INT, degree_of_certainty=NEG_INT)]
            indicator.update(assessments=[])
