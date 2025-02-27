flowchart TD 
    %% Define nodes with classes for color styling
    UI["User Interface Module"]:::uiStyle
    MAIN["Main Application Orchestrator"]:::mainStyle
    CORE["Core Processing Module"]:::coreStyle
    TEST["Testing Suite"]:::testStyle

    %% Vertical Layout: Data Flow from UI to Main to Core and back, plus testing validations
    UI -->|"sendsInput"| MAIN
    MAIN -->|"delegatesProcessing"| CORE
    CORE -->|"returnsOutput"| MAIN
    MAIN -->|"updatesUI"| UI
    TEST -->|"validatesCore"| CORE
    TEST -->|"validatesMain"| MAIN

    %% Click Events based on component mapping
    click UI "https://github.com/milliegw/enigmamachinemsc/tree/main/EnigmaMachine/ui"
    click MAIN "https://github.com/milliegw/enigmamachinemsc/blob/main/EnigmaMachine/enigma.py"
    click CORE "https://github.com/milliegw/enigmamachinemsc/tree/main/EnigmaMachine/core"
    click TEST "https://github.com/milliegw/enigmamachinemsc/tree/main/EnigmaMachine/tests"

    %% Styling classes with colors
    classDef uiStyle fill:#FFC0CB,stroke:#333,stroke-width:2px;
    classDef mainStyle fill:#90EE90,stroke:#333,stroke-width:2px;
    classDef coreStyle fill:#ADD8E6,stroke:#333,stroke-width:2px;
    classDef testStyle fill:#FFD700,stroke:#333,stroke-width:2px;
