import pandas as pd

from src.models.indicators import CodeAndDescription, Indicator

EMPTY = ""

df = pd.read_excel("./xlsx/adaptation.xlsx", sheet_name="Final Flexible superset")
df = df.fillna(EMPTY)
for _, row in df.iterrows():
    indicator_code = row["name"].split(" ")[0]
    indicator_category_code = row["category"].split(" ")[0]
    indicator_subcategory_code = row["subcategory"].split(" ")[0]
    description = row["name"].split(" ", 1)[1]
    category_description = row["category"].split(" ")[1]
    subcategory_description = row["subcategory"].split(" ")[1]
    principal = row["principal"]
    main_climate_change_factor = row["main_climate_change_factor"]
    other_climate_change_factors = row["other_climate_change_factors"]
    main_affected_sector = row["main_affected_sector"]
    other_affected_sectors = row["other_affected_sectors"]
    type = row["type"]
    metrics_and_units = row["metrics_and_units"]
    spatial_scale = row["spatial_scale"]
    references = row["references"]
    typology = row["typology"]
    category = CodeAndDescription(
        code=indicator_category_code, description=category_description
    )
    subcategory = CodeAndDescription(
        code=indicator_subcategory_code, description=subcategory_description
    )
    indicator = Indicator(
        code=indicator_code,
        description=description,
        principal=principal,
        main_climate_change_factor=main_climate_change_factor,
        other_climate_change_factors=other_climate_change_factors,
        main_affected_sector=main_affected_sector,
        other_affected_sectors=other_affected_sectors,
        type=type,
        metrics_and_units=metrics_and_units,
        spatial_scale=spatial_scale,
        references=references,
        typology=typology,
        category=category,
        subcategory=subcategory,
        kind="adaptation",
        definedBy="IMPETUS",
    )
    try:
        Indicator.objects(code=indicator_code).update_one(
            **indicator.to_mongo(), upsert=True
        )
    except Exception:
        print("failed")
