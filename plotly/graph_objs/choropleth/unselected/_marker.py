from plotly.basedatatypes import BaseTraceHierarchyType


class Marker(BaseTraceHierarchyType):

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the marker opacity of unselected points, applied only when
        a selection exists.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'choropleth.unselected'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        opacity
            Sets the marker opacity of unselected points, applied
            only when a selection exists.
        """

    def __init__(self, arg=None, opacity=None, **kwargs):
        """
        Construct a new Marker object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.choropleth.unselected.Marker
        opacity
            Sets the marker opacity of unselected points, applied
            only when a selection exists.

        Returns
        -------
        Marker
        """
        super(Marker, self).__init__('marker')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.choropleth.unselected.Marker 
constructor must be a dict or 
an instance of plotly.graph_objs.choropleth.unselected.Marker"""
            )

        # Import validators
        # -----------------
        from plotly.validators.choropleth.unselected import (
            marker as v_marker
        )

        # Initialize validators
        # ---------------------
        self._validators['opacity'] = v_marker.OpacityValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('opacity', None)
        self.opacity = opacity or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
