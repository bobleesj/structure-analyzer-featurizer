How to SAF CAF App
==================

The SAF App (`GitHub <https://github.com/bobleesj/structure-analyzer-featurizer-app>`_) offers a single option

.. note::

   The installation guide is provided in :ref:`SAF-app-installation`.

**Option 1. Filter** - analyze chemical formulas in Excel or a folder of ``.cif`` files. Counts unique elements, detects errors, generates a periodic table heatmap, and provides filtering methods.

.. image:: img/periodic-table-heatmap.png
   :alt: periodic table heatmap

**Option 2. Sort** - rearrange chemical formulas in Excel by:

1. **Label** (pre-configured for binary/ternary compounds, editable in ``data/sort/custom-labels.xlsx``)
2. **Index** (stoichiometric ratio, then Mendeleev number)
3. **Property** (27 elemental properties from the Oliynyk database)

Available columns for sorting:

.. code-block:: text

   1. Atomic weight
   2. Atomic number
   3. Period
   4. Group
   5. Mendeleev number
   6. valence e total
   7. unpaired electrons
   8. Gilman no. of valence electrons
   9. Zeff
   10. Ionization energy (eV)
   11. CN
   12. ratio n closest/CN
   13. polyhedron distortion (dmin/dn)
   14. CIF radius element
   15. Pauling, R(CN12)
   16. Pauling EN
   17. Martynov Batsanov EN
   18. Melting point, K
   19. Density, g/mL
   20. Specific heat, J/g K
   21. Cohesive energy
   22. Bulk modulus, GPa
   23. Abundance in Earth's crust
   24. Abundance in solar system (log)
   25. HHI production
   26. HHI reserve
   27. cost, pure ($/100g)

**Option 3. Features** - generate compositional features for formulas in Excel, including a composition-normalized vector using hot encoding. The database is based on the Oliynyk (OLED) data (`DOI <https://doi.org/10.1016/j.dib.2024.110178>`_).

- 133 binary features (``features/binary.py``)
- 204 ternary features (``features/ternary.py``)
- 305 quaternary features (``features/quaternary.py``)
- Universal set of 112 sorted and 156 unsorted features (``feature/universal.py``)
- (Optional) Extended features (thousands of columns possible)

Example of ``feature_binary.xlsx``:

+---------+---------+---------+--------------------+--------------------+---------------+----------------+-----------+------------------------------+
| Formula | index_A | index_B | normalized_index_A | normalized_index_B | largest_index | smallest_index | avg_index | atomic_weight_weighted_A+B   |
+=========+=========+=========+====================+====================+===============+================+===========+==============================+
| NdSi2   | 1       | 2       | 0.333              | 0.667              | 2             | 1              | 1.5       | 144.242                      |
+---------+---------+---------+--------------------+--------------------+---------------+----------------+-----------+------------------------------+
| Th2Os   | 2       | 1       | 0.667              | 0.333              | 2             | 1              | 1.5       | 464.076                      |
+---------+---------+---------+--------------------+--------------------+---------------+----------------+-----------+------------------------------+
| Sn5Co2  | 5       | 2       | 0.714              | 0.286              | 5             | 2              | 3.5       | 593.55                       |
+---------+---------+---------+--------------------+--------------------+---------------+----------------+-----------+------------------------------+

**Option 4. Match** - match ``.cif`` files in a folder against an Excel file by the "Entry" column.

**Option 5. Merge** - combine two Excel files based on the "Entry" column.
