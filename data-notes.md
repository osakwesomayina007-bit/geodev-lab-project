<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/79ecdc09-47b5-4af5-b546-1b7d0416061e" /># Data Notes

## OSM Sport Facilities, Eti-Osa, Lagos

- Source: OpenStreetMap, via QuickOSM
- Downloaded: 12 September 2026
- CRS: EPSG:4326 - WGS 84
- Study area: Eti-Osa Local Government Area, Lagos State, Nigeria

### sports_pitches.gpkg

- 221 features, polygons (MultiPolygon)
- Columns: full_id, osm_id, osm_type, leisure, lit, surface, name, access, building, sport (all text)
- Nulls: lit, surface, name, access, and building contain many NULL values; sport is populated for most rows
- Coverage looks decent for mapped pitches, but many features lack surface and access details
- Suitable for identifying mapped sports pitches and their locations

### sports_pitches_points.gpkg

- 1 feature, point
- Columns: full_id, osm_id, osm_type, leisure, sport (all text)
- No NULL values in the displayed attributes
- Contains one point-mapped basketball pitch
- Kept as a separate point layer for checking additional mapped facilities

### sports_centres.gpkg

- 5 features, polygons (MultiPolygon)
- Columns: full_id, osm_id, osm_type, leisure, surface, wikipedia, wikidata, sport, name (all text)
- Nulls: surface, wikipedia, wikidata, and sport contain many NULL values; name is populated for most features
- Very sparse, with only five mapped sports centres in the extracted dataset
- Useful for identifying mapped sports centres, but may not represent all sports centres in the study area

### sports_centres_points.gpkg

- 1 feature, point
- Columns: full_id, osm_id, osm_type, leisure, sport, name (all text)
- No NULL values in the displayed attributes
- Contains one point-mapped sports centre, Ikoyi Club, with swimming as the sport
- Kept as a separate point layer for checking additional mapped facilities

### stadiums.gpkg

- 2 features, polygons (MultiPolygon)
- Columns: full_id, osm_id, osm_type, leisure, wikipedia, wikidata, name (all text)
- Nulls: the Mobolaji Johnson/Onikan Stadium record contains wikipedia and wikidata information, while the Campos Memorial Stadium record has NULL values in these fields
- Only two stadiums are captured in the extracted dataset, so the actual number of stadiums in the study area may be higher
- Useful for identifying mapped stadiums as part of the sports facility analysis

### park.gpkg

- 16 features, polygons (MultiPolygon)
- Columns: full_id, osm_id, osm_type, leisure, wikipedia, addr_stree, addr_house, addr_city, Lagos_Isla, Creative_L, wikidata, name (all text)
- Nulls: most attribute columns contain NULL values; a few features have names and additional information
- Coverage is uneven, with some parks richly tagged and others containing mainly geometry and leisure=park
- Suitable for identifying mapped parks and assessing their spatial distribution

### park_points.gpkg

- 1 feature, point
- Columns: full_id, osm_id, osm_type, leisure, wikidata, name, is_in_country, GNS_id, GNS_dsg_st, GNS_dsg_co (all text)
- No NULL values in the displayed attributes
- Contains one point-mapped park, Ikoyi Park, with additional gazetteer information
- Kept as a separate point layer for checking additional mapped parks

### roads.gpkg

- 14,636 features, lines (MultiLineString)
- Columns: full_id, osm_id, osm_type, highway, man_made, locked, ford, turn_lanes, lanes_forw, lanes_back, maxspeed_f, hide, width, maxheight, closed, barrier, covered (all text)
- Nulls: highway is consistently populated in the displayed records, while most other attributes contain many NULL values
- Road classification information is available through the highway field, but detailed attributes such as lanes, speed limits, and width are largely missing
- Coverage looks good for the mapped road network, although the completeness of coverage should be checked against the study area
- Suitable for supporting accessibility analysis, particularly when combined with community boundaries and facility locations

## Eti-Osa Boundary Dataset

## NGA_LGA_Boundaries_2_2960381615559861217.gpkg

- Source: Nigerian Local Government Area boundary dataset
- Study area: Eti-Osa LGA, Lagos State, Nigeria
- CRS: EPSG:4326 - WGS 84
- Geometry: Polygon (MultiPolygon)
- Feature count: 774 features
- Relevant fields: `FID`, `globalid`, `uniq_id`, `lganame`, `lgacode`, `statename`, `statecode`, `source`, and `amapcode`
- Eti-Osa record: `lganame = Eti Osa`, `lgacode = 25008`, `statename = Lagos`
- The boundary layer will be used to isolate Eti-Osa from the wider LGA dataset, define the study area, and clip the sports facility and road layers. The boundary should be extracted and checked before further analysis.

## Overall Data Assessment

- The datasets provide a useful starting point for assessing access to mapped parks and sports facilities in Eti-Osa.
- The polygon layers will be the main facility datasets, while the point layers will be retained for checking additional mapped facilities.
- OpenStreetMap coverage may be incomplete, so the analysis will describe access to mapped facilities rather than every facility in the study area.
- The Eti-Osa LGA boundary dataset provides the geographic framework for defining the study area and limiting the analysis to the selected local government area.
- The community or ward boundary layer for Eti-Osa is required to compare accessibility between communities.
- The road network can support accessibility analysis, but missing road attributes may limit detailed road classification or routing.
- The project remains feasible because the available datasets provide mapped facilities, roads, and an LGA boundary. However, the completeness of the OSM data and the availability of community or ward boundaries will affect the accuracy and level of detail of the final accessibility assessment.


# Data Preparation and Quality Notes

## Study area

- Study area: Eti-Osa Local Government Area, Lagos State, Nigeria
- Study area source: GRID3 administrative boundary data
- Study area area check: 177.9 km², matching the published value used for the check
- Original source layers were provided in EPSG:4326.

## CRS and preparation

- Original CRS: EPSG:4326 (WGS 84)
- Working CRS: EPSG:32631 (WGS 84 / UTM Zone 31N)
- EPSG:32631 was chosen because the study area is in western Nigeria and the projected CRS uses metres, making it suitable for distance and area calculations.
- Roads, sports pitches and sports centres were clipped to the Eti-Osa study area.
- The study area and other required layers were reprojected to EPSG:32631.
- The original files in `data/raw/` were not modified.
- The analysis-ready files were saved in `data/processed/`.

# Data Quality Notes

## Study area — GRID3 Eti-Osa boundary
- Source: GRID3 administrative boundary data
- CRS: EPSG:4326; reprojected to EPSG:32631 (WGS 84 / UTM Zone 31N) for analysis.
- COMPLETENESS: Eti-Osa LGA boundary was present and used as the study area. No obvious gaps or duplicate study-area features were observed.
- CURRENCY: Boundary was checked against available reference information. No obvious changes affecting the study area were identified.
- POSITIONAL: Boundary was visually checked against satellite imagery; no major positional offset was observed.
- ATTRIBUTE: LGA name and identifying attributes were checked; the study area was correctly identified as Eti Osa.
- FITNESS: Suitable for defining the study area and clipping the other datasets.

## OSM roads, Eti-Osa
- Source: OpenStreetMap via QuickOSM, `highway=*`
- COMPLETENESS: Roads were checked against satellite imagery in the study area. Most visible roads in the areas checked were represented in the dataset.
- CURRENCY: OpenStreetMap data is continuously updated, so a single dataset year was not assigned. The extracted data represents the OSM data available when it was downloaded.
- POSITIONAL: Roads were visually compared with satellite imagery and generally aligned with visible road locations.
- ATTRIBUTE: Road attributes were inspected for missing and varied values. No major attribute issue affecting the intended analysis was identified.
- FITNESS: Suitable for general road network and accessibility analysis within Eti-Osa, but may not represent every road or indicate current road condition.

## OSM sports pitches, Eti-Osa
- Source: OpenStreetMap via QuickOSM, sports pitches
- COMPLETENESS: Sports pitches were checked against satellite imagery. Most visible sports facilities in the areas checked were represented, although facilities may be missing where they are not mapped in OSM or are difficult to identify from imagery.
- CURRENCY: No single year was assigned because the data was extracted from OpenStreetMap, which is continuously updated. The dataset represents the OSM data available when it was downloaded.
- POSITIONAL: Sports pitches were visually checked against satellite imagery and generally corresponded with the visible facilities.
- ATTRIBUTE: Fields such as sport, access, building and name were inspected. Some attributes contain NULL values, which were retained where no reliable information was available.
- FITNESS: Suitable for analysing the distribution and location of mapped sports pitches in Eti-Osa. It should not be assumed to represent every existing sports pitch.

## OSM sports centres, Eti-Osa
- Source: OpenStreetMap via QuickOSM, sports centres
- COMPLETENESS: Sports centres were checked against satellite imagery in the study area. No major missing groups were identified during the areas checked.
- CURRENCY: No single year was assigned because the data was extracted from continuously updated OpenStreetMap. The dataset represents the OSM data available when it was downloaded.
- POSITIONAL: Features were visually checked against satellite imagery and generally aligned with the mapped locations.
- ATTRIBUTE: Available attributes were inspected for missing or inconsistent values. No major issue affecting the intended analysis was identified.
- FITNESS: Suitable for analysing the location and distribution of mapped sports centres within the study area.

## OSM parks, Eti-Osa
- Source: OpenStreetMap via QuickOSM, `leisure=park`
- COMPLETENESS: Parks were checked against satellite imagery in the study area. Most visible parks in the areas checked were represented, although some may be missing where they are not mapped in OSM or are difficult to identify from imagery.
- CURRENCY: No single year was assigned because the data was extracted from OpenStreetMap, which is continuously updated. The dataset represents the OSM data available when it was downloaded.
- POSITIONAL: Parks were visually compared with satellite imagery and generally corresponded with the visible park locations.
- ATTRIBUTE: Available attributes such as name and other descriptive fields were inspected. Some attributes contain NULL values, which were retained where no reliable information was available.
- FITNESS: Suitable for analysing the distribution and location of mapped parks in Eti-Osa. It should not be assumed to represent every existing park.

## OSM stadiums, Eti-Osa
- Source: OpenStreetMap via QuickOSM,`leisure=stadium`
- COMPLETENESS: Stadiums were checked against satellite imagery in the study area. The mapped stadiums in the areas checked were represented, although unmapped facilities may not be included.
- CURRENCY: No single year was assigned because the data was extracted from OpenStreetMap, which is continuously updated. The dataset represents the OSM data available when it was downloaded.
- POSITIONAL: Stadiums were visually compared with satellite imagery and generally corresponded with their visible locations.
- ATTRIBUTE: Available attributes such as name, sport and other descriptive fields were inspected. Some attributes contain NULL values, which were retained where no reliable information was available.
- FITNESS: Suitable for analysing the location and distribution of mapped stadiums within Eti-Osa. It should not be assumed to represent every existing stadium.

## Preparation
- All required layers were clipped to the Eti-Osa study area.
- Layers were reprojected from EPSG:4326 to EPSG:32631 (WGS 84 / UTM Zone 31N).
- Study area check: 177.9 km², matching the published reference value used for the check.
- Original source data in `data/raw/` was not modified.
- Analysis-ready GeoPackages are stored in `data/processed/`.

## Problems found and actions taken

- Source layers were in EPSG:4326, so they were reprojected to EPSG:32631 for analysis.
- Roads and sports facility layers were clipped to the Eti-Osa study area.
- The original raw datasets were preserved.
- Area calculations were checked after reprojection using square metres and square kilometres.
- The calculated Eti-Osa study area was 177.9 km² and was checked against the published reference value.
- No major data quality problems requiring removal of features were identified. Uncertain or missing attribute information was flagged rather than guessed.



