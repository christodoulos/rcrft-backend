import pandas as pd

from src.models.indicators import Indicator, CodeAndDescription

EMPTY = ""

df = pd.read_excel("./xlsx/adaptation.xlsx", sheet_name="Final Flexible superset")
for _, row in df.iterrows():
    # print(row)
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
    data_requirements = row["data_requirements"]
    references = row["references"]
    typology = row["typology"]
    category = CodeAndDescription(
        code=indicator_category_code,
        description=category_description
        if not isinstance(category_description, float)
        else EMPTY,
    )
    subcategory = CodeAndDescription(
        code=indicator_subcategory_code,
        description=subcategory_description
        if not isinstance(subcategory_description, float)
        else EMPTY,
    )
    indicator = Indicator(
        code=indicator_code if not isinstance(indicator_code, float) else EMPTY,
        description=description if not isinstance(description, float) else EMPTY,
        principal=principal if not isinstance(principal, float) else EMPTY,
        main_climate_change_factor=main_climate_change_factor
        if not isinstance(main_climate_change_factor, float)
        else EMPTY,
        other_climate_change_factors=other_climate_change_factors
        if not isinstance(other_climate_change_factors, float)
        else EMPTY,
        main_affected_sector=main_affected_sector
        if not isinstance(main_affected_sector, float)
        else EMPTY,
        other_affected_sectors=other_affected_sectors
        if not isinstance(other_affected_sectors, float)
        else EMPTY,
        type=type if not isinstance(type, float) else EMPTY,
        metrics_and_units=metrics_and_units
        if not isinstance(metrics_and_units, float)
        else EMPTY,
        spatial_scale=spatial_scale if not isinstance(spatial_scale, float) else EMPTY,
        data_requirements=data_requirements
        if not isinstance(data_requirements, float)
        else EMPTY,
        references=references if not isinstance(references, float) else EMPTY,
        typology=typology if not isinstance(typology, float) else EMPTY,
        category=category if not isinstance(category, float) else EMPTY,
        subcategory=subcategory if not isinstance(subcategory, float) else EMPTY,
        kind="vulnerability",
    ).save()
