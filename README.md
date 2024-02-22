# H3D virtual screening cascade light

This panel of models provides predictions for the H3D virtual screening cascade. It leverages the Ersilia Compound Embedding and FLAML. The H3D virtual screening cascade contains models for Mycobacterium tuberculosis and Plasmodium falciparum IC50 predictions, as well as ADME, cytotoxicity and solubility assays

## Identifiers

* EOS model ID: `eos7kpb`
* Slug: `h3d-virtual-screening-cascade-light`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: The raw scores are the ones emerging from the FLAML model. The ones with a sufix _perc represent the percentile in the scale 0-1 over a ChEMBL dataset of 200k compounds.

## References

* [Publication](https://www.nature.com/articles/s41467-023-41512-2)
* [Source Code](https://github.com/ersilia-os/h3d-screening-cascade-models)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos7kpb)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos7kpb.zip)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s41467-023-41512-2) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!