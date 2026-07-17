<annotation> <!-- The "root" (the main filing cabinet) -->

    <size>                     <!-- The "size" folder -->
        <width>640</width>     <!-- root.find("size").find("width") -->
        <height>480</height>    <!-- root.find("size").find("height") -->
    </size>

    <object>                   <!-- An "object" folder (Item #1) -->
        <name>helmet</name>    <!-- obj.find("name") -> The Class Label -->
        <bndbox>               <!-- The "bndbox" sub-folder (Bounding Box) -->
            <xmin>50</xmin>    <!-- bbox_tag.find("xmin") -->
            <ymin>60</ymin>    <!-- bbox_tag.find("ymin") -->
            <xmax>120</xmax>   <!-- bbox_tag.find("xmax") -->
            <ymax>130</ymax>   <!-- bbox_tag.find("ymax") -->
        </bndbox>
    </object>

    <object>                   <!-- Another "object" folder (Item #2) -->
        <name>person</name>
        <bndbox>
            <xmin>200</xmin>
            <ymin>150</ymin>
            <xmax>350</xmax>
            <ymax>400</ymax>
        </bndbox>
    </object>

</annotation>
