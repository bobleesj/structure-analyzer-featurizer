.. _getting-started:

Getting started
===============

The recommended way is to use the SAF app, a command-line interface (CLI) application that can automatically detect folders containing ``.cif`` files.

.. _SAF-app-installation:

Method 1. Using SAF Application
-------------------------------

First, download the SAF application from the GitHub repository. You can clone (download) the files using the following command:

.. code-block:: bash

   git clone https://github.com/bobleesj/structure-analyzer-featurizer-app.git

.. note::

   Alternatively, you can download the ZIP file from the GitHub repository (https://github.com/bobleesj/structure-analyzer-featurizer-app) by clicking the green :guilabel:`Code` button and :guilabel:`Download ZIP`. After downloading, extract the contents of the ZIP file to a directory of your choice.

Next, navigate to the directory and install the required package using pip:

.. code-block:: bash

   cd structure-analyzer-featurizer-app
   pip install structure-analyzer-featurizer

You can then run the application by executing the following command:

.. code-block:: bash

   python main.py

Upon running ``python main.py``, you will be prompted to choose from one of the following options:

.. code-block:: text

    Folders with .cif files detected:
    1. 20240902_PCD_demo_files (20 files)
    2. 20240902_ICSD_demo_files (20 files)

    Would you like to process each folder above sequentially?
    (Default: Y) [Y/n]:

Press ``Enter`` to generate structure features for the ``.cif`` files in the chosen folder. At the end, ``.csv`` files will be saved in the chosen project directory, including ``csv/<composition-type>_features.csv`` and ``csv/universal_features.csv``.

.. note::

   Are you having trouble running code? Learn to use conda environments by following the instructions provided `here <https://scikit-package.github.io/scikit-package/tutorials/tutorial-level-1-2-3.html#required-use-conda-environment-to-install-packages-and-run-python-code>`_.

Method 2. Import SAF in Python file or Jupyter notebook
-------------------------------------------------------

You might be interested in generating compositional features without using the SAF application.

.. code-block:: bash

   pip install structure-analyzer-featurizer

This will install key packages such as ``cifkit`` and ``bobleesj.utils`` that are required to run the SAF package. Then, you can generate features by calling the function provided in the SAF package directly.

.. code-block:: python

    from cifkit import Cif
    from SAF.features.generator import (
        compute_binary_features,
        compute_quaternary_features,
        compute_ternary_features,
    )
    try:
        if len(cif.unique_elements) == 2:
            features, uni_features = compute_binary_features(file_path)
            binary_data.append(features)
        if len(cif.unique_elements) == 3:
            features, uni_features = compute_ternary_features(file_path)
            ternary_data.append(features)
        if len(cif.unique_elements) == 4:
            features, uni_features = compute_quaternary_features(file_path)
    except Exception as e:
        print(f"Error found for {file_path}. Reason: {e}")


How can I specify the elements for ``A``, ``B`` in binary, ``R``, ``M``, ``X`` in ternary, and ``A``, ``B``, ``C``, ``D`` in quaternary systems?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, ``SAF`` automatically orders the elements from highest to lowest Mendeleev number. The Mendeleev number for each element is parsed from the ``bobleesj.utils`` `Python package <https://bobleesj.github.io/bobleesj.utils>`_. If you want to specify the order of the elements, you can provide a custom label mapping dictionary to the ``compute_binary_features``, ``compute_ternary_features``, or ``compute_quaternary_features`` functions, as shown below.

.. code-block:: python

    custom_labels = {
        2: {"A": ["Fe", "Co"], "B": ["Si", "Ga"]},
        3: {"R": ["Sc", "Y"], "M": ["Fe", "Co"], "X": ["Si", "Ga"]},
        4: {"A": ["Sc", "Y"], "B": ["Fe", "Co"], "C": ["Si", "Ga"], "D": ["Gd", "Tb", "Dy"]},
    }

    file_path = "path/to/your/cif_file.cif"
    compute_binary_features(file_path, custom_labels=custom_labels)

Alternatively, you can provide a custom label mapping dictionary using this `template Excel file <https://github.com/bobleesj/bobleesj.utils/blob/main/tests/data/sort/test-custom-labels.xlsx>`_ and the ``ElementSorter`` class from the ``bobleesj.utils.sorters.element_sorter`` module:

.. code-block:: python

    from bobleesj.utils.sorters.element_sorter import ElementSorter

    excel_file = "path/to/your/custom_labels.xlsx"
    element_sorter = ElementSorter(excel_path=excel_file)
    custom_labels = element_sorter.label_mapping
    compute_binary_features(file_path, custom_labels=custom_labels)
