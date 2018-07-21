import _plotly_utils.basevalidators


class ColorscaleValidator(_plotly_utils.basevalidators.ColorscaleValidator):

    def __init__(
        self, plotly_name='colorscale', parent_name='bar.marker', **kwargs
    ):
        super(ColorscaleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            implied_edits={'autocolorscale': False},
            role='style',
            **kwargs
        )