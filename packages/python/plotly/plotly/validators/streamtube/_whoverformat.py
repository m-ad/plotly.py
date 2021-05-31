import _plotly_utils.basevalidators


class WhoverformatValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="whoverformat", parent_name="streamtube", **kwargs):
        super(WhoverformatValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs
        )