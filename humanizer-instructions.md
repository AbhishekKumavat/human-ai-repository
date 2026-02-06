I have made the following changes to the codebase:

1.  **Model Downloading**: I've modified `download_models.py` to save all downloaded models into a `models` directory inside the `Humanizer-main` folder. This keeps all the models organized in one place within the project.

2.  **Model Loading**: I've updated `paraphraser.py` and `detector.py` to load the necessary models from this new `models` directory. This ensures that the application uses the locally downloaded models.

To get the application running, you will need to do the following:

1.  **Download the models**: Run the following command from the `f:\Humanizer-main` directory in your terminal:
    ```
    python Humanizer-main/download_models.py
    ```

2.  **Install dependencies**: The application requires some additional Python packages. Please install them by running:
    ```
    pip install spacy textblob
    ```

3.  **Download language model**: The `rewriter.py` script also needs a language model from `spacy`. Please download it by running:
    ```
    python -m spacy download en_core_web_sm
    ```

After these steps, the application should be ready to use.
