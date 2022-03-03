import datatools


def main(data: datatools.datasources.DataSource, transformer: datatools.transformers.Transformer):
    raw_data = data.raw_data

    transformer = datatools.transformers.Transformer(  # Takes multiple functions, each a separate argument
        ...
    )

    raw_data.transform(transformer)
    transformed_data = data.transformed_data

