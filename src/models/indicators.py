import mongoengine as me


class CodeAndDescription(me.EmbeddedDocument):
    code = me.StringField()
    description = me.StringField()


class Indicator(me.Document):
    meta = {"collection": "indicators", "db_alias": "rcrft"}

    definedBy = me.StringField(required=True, default="IMPETUS")
    category = me.EmbeddedDocumentField(CodeAndDescription)
    subcategory = me.EmbeddedDocumentField(CodeAndDescription)
    code = me.StringField()
    description = me.StringField()
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
    kind = me.StringField(choices=["vulnerability", "adaptation"], unique_with="code")
