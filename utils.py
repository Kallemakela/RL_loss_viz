def apply_style(df, precision=2):
    def align_pn(x):
        return "text-align: right;"

    return (
        df.style.format(precision=precision)
        .background_gradient(cmap="RdYlGn_r", axis=None)
        .map(align_pn)
        .set_table_styles(
            [
                {
                    "selector": "th",
                    "props": [("background-color", "#333333"), ("color", "#FFFFFF")],
                }
            ]
        )
    )
