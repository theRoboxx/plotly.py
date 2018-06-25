from plotly.basedatatypes import BaseLayoutHierarchyType


class Aspectratio(BaseLayoutHierarchyType):

    # x
    # -
    @property
    def x(self):
        """
        The 'x' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['x']

    @x.setter
    def x(self, val):
        self['x'] = val

    # y
    # -
    @property
    def y(self):
        """
        The 'y' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['y']

    @y.setter
    def y(self, val):
        self['y'] = val

    # z
    # -
    @property
    def z(self):
        """
        The 'z' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['z']

    @z.setter
    def z(self, val):
        self['z'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.scene'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        x

        y

        z

        """

    def __init__(self, arg=None, x=None, y=None, z=None, **kwargs):
        """
        Construct a new Aspectratio object
        
        Sets this scene's axis aspectratio.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            plotly.graph_objs.layout.scene.Aspectratio
        x

        y

        z


        Returns
        -------
        Aspectratio
        """
        super(Aspectratio, self).__init__('aspectratio')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif not isinstance(arg, dict):
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.scene.Aspectratio 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.scene.Aspectratio"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.scene import (
            aspectratio as v_aspectratio
        )

        # Initialize validators
        # ---------------------
        self._validators['x'] = v_aspectratio.XValidator()
        self._validators['y'] = v_aspectratio.YValidator()
        self._validators['z'] = v_aspectratio.ZValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('x', None)
        self.x = x or v
        v = arg.pop('y', None)
        self.y = y or v
        v = arg.pop('z', None)
        self.z = z or v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
