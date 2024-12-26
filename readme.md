<img width="100px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Tehran_Metro_Logo.svg/200px-Tehran_Metro_Logo.svg.png"/>

# Tehran Metro Graph Data

This repository contains data related to the Tehran Metro stations. The data is available in JSON format as a graph structure data, providing different options for utilizing the data.

## Repository Contents

1. `data/stations.json`: This file contains the Tehran Metro stations data in JSON format. It includes information such as station names, coordinates, and other relevant details.

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
        "name": "Tajrish",
        "fa": "تجریش",
        "lines": [1],
        "longitude": "51.433643000000004",
        "latitude": "35.804501",
        "address": "خیابان شریعتی-ضلع جنوب غربی میدان قدس",
        "wc": false,
        "coffeeShop": false,
        "groceryStore": false,
        "fastFood": false,
        "atm": false,
        "relations": ["Gheytariyeh"]
    },
    ...
}
```

### Station Relations

Each station can have relations with other stations. These relations are represented as an array of names within the station object.

Example:

```json
{
    "Gheytariyeh": {
        ...
        "relations": ["Tajrish", "Shahid Sadr"]
    },
    ...
}
```

## License

The data in this repository is licensed under the [Open Data Commons License](https://opendatacommons.org/licenses/). Please refer to the license file for more details on the terms and conditions of using the data.

If you have any questions or suggestions regarding the data or this repository, feel free to open an issue or contact me
