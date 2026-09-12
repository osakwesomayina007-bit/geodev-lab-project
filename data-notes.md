# Data Notes

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
