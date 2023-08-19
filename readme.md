# Tehran Metro Stations Data Repository

This repository contains data related to the Tehran Metro stations. The data is available in both JSON format and Neo4j database format, providing different options for utilizing the data.

## Repository Contents

1. `data/stations.json.json`: This file contains the Tehran Metro stations data in JSON format. It includes information such as station names, coordinates, and other relevant details.

2. `data/neo4j.stations.json.`: This file contains the Tehran Metro stations data in the Neo4j json database format. The Neo4j format allows for storing and querying graph data, which can be useful for analyzing the relationships between different metro stations.

## Data Structure (data/stations.json)

The data in this repository follows a specific structure to represent the Tehran Metro stations. Here's an overview of the structure:

### Station Properties

Each station is represented by an object containing the following properties:

- `"disabled"`: A boolean value indicating if the station is disabled or not.
- `"name"`: The name of the station in English.
- `"fa"`: The name of the station in Persian (Farsi).
- `"colors"`: An array of color codes associated with the station. This can be used to represent the station on maps or in visualizations.
- `"lines"`: An array of line numbers associated with the station. This indicates the metro lines that pass through the station.

Example:

```json
{
    "Tajrish": {
        "property": {
            "disabled": false,
            "name": "Tajrish",
            "fa": "تجریش",
            "colors": ["#E0001F"],
            "lines": [1]
        },
        ...
    },
    ...
}
```

### Station Relations

Each station can have relations with other stations. These relations are represented as an array of objects within the station object. Each relation object contains similar properties to the station object, including:

- `"name"`: The name of the related station in English.
- `"disabled"`: A boolean value indicating if the related station is disabled or not.
- `"fa"`: The name of the related station in Persian (Farsi).
- `"colors"`: An array of color codes associated with the related station.
- `"lines"`: An array of line numbers associated with the related station.

Example:

```json
{
    "Tajrish": {
        "property": {
            ...
        },
        "relations": [
            {
                "name": "Gheytariyeh",
                "disabled": false,
                "fa": "قیطریه",
                "colors": ["#E0001F"],
                "lines": [1]
            },
            ...
        ]
    },
    ...
}
```

This structure allows for representing stations, their properties, and their relations in a structured and organized manner. You can use this data to build applications, perform analyses, or create visualizations related to the Tehran Metro stations.

Please note that this is just an example based on the data you provided. You may need to adjust the structure and properties to fit your specific data requirements and use cases.

## License

The data in this repository is licensed under the [Open Data Commons License](https://opendatacommons.org/licenses/). Please refer to the license file for more details on the terms and conditions of using the data.

If you have any questions or suggestions regarding the data or this repository, feel free to open an issue or contact me
