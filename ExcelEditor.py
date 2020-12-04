import CsvToXlsx
from tkinter import messagebox


def create():
    file_names = ["UK", "DE", "FR", "IT", "ES"]
    for file_name in file_names:
        csv_file = open(file_name + ".csv", "x")
        csv_file.write(
            "TemplateType=fptcustom;Version=2019.0519;Templatpedito;dallo;stesso;giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Eignature=U0hJUlQ=;The;top;3;rows;are;for;Amazon.com;use;only.;Do;not;modify;or;delete;the;top;3;rows.;;;;;;;;;;;;;;;Imagpedito;dallo;stesso;giorno.;;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;E;;;;;;;;Variation;;;;Basic;;;;;;;;Discovery;;;;;;;;;;;;;;;;;Product;Enrichment;;;;Dimensions;;;;;;;;;Fulfillment;;;;;;;Compliance;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;Offer;;;;;;;;;;;;;;;;;;;;;;;b2b\n")
        csv_file.write(
            "Product Type;;Brand Name;Product ID;Product ID Type;Product Name;Recommended Browse Nodes;Outer Material Type;Material Composition;Colour Map;Colour;Size;Department;Size Map;Adult Flag;Standard Price;Quantity;Main Image Url;Other Image Url1;Other Image Url2;Other Image Url3;Other Image Url4;Other Image Url5;Other Image Url6;Other Image Url7;Other Image Url8;Parentage;Parent SKU;Relationship Type;Variation Theme;Update Delete;Product Description;Inner Material Type;Product Care Instructions;Model Name;Model Number;Manufacturer Part Number;Product Exemption Reason;Search Terms;Season and collection year;Pattern description;Occasion description;Fitting type;Key Product Features;Key Product Features;Key Product Features;Key Product Features;Key Product Features;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;platinum-keywords1 - platinum-keywords5;Season;material_type;Style Name;Sleeve Type;Collar Style;size-modifier;Neck size;Neck Size unit;Shipping Weight;Website Shipping Weight Unit Of Measure;Item Width;Item Height;Item Shape;Item Dimensions Unit Of Measure;Item Length;Fulfillment Centre ID;Package Length;package-width;Package Height;Package Weight;Package Weight Unit Of Measure;Package Dimensions Unit Of Measure;Legal Disclaimer Description;Safety Warning;EU Toys Safety Directive Age-specific warning;EU Toys Safety Directive Non-Age-specific warning;EU Toys Safety Directive language warning;Country/Region Of Origin;Is this product a battery or does it utilise batteries?;Batteries are Included;Battery composition;Battery type/size;Battery type/size;Battery type/size;Number of batteries;Number of batteries;Number of batteries;Battery weight (grams);battery_weight_unit_of_measure;Number of Lithium Metal Cells;Number of Lithium-ion Cells;Lithium Battery Packaging;Watt hours per battery;lithium_battery_energy_content_unit_of_measure;Lithium content (grams);lithium_battery_weight_unit_of_measure;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;Applicable Dangerous Goods Regulations;UN number;Safety Data Sheet (SDS) URL;Item Weight;item_weight_unit_of_measure;Volume;item_volume_unit_of_measure;Flash point (°C)?;Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Categorization/GHS pictograms (select all that apply);Condition Type;condition_note;Currency;Handling Time;Sale Price;Sale From Date;Sale End Date;max-aggregate-ship-quantity;Package Quantity;Number of Items;Can Be Gift Messaged;Is Gift Wrap Available?;Is Discontinued by Manufacturer;Launch Date;Restock Date;Recommended Retail Price;Stop Selling Date;Max Order Quantity;Merchant Shipping Group;Offering Release Date;Scheduled Delivery SKU List;RRP;Product Tax Code;Business Price;Quantity Price Type;Quantity Lower Bound 1;Quantity Price 1;Quantity Lower Bound 2;Quantity Price 2;Quantity Lower Bound 3;Quantity Price 3;Quantity Lower Bound 4;Quantity Price 4;Quantity Lower Bound 5;Quantity Price 5;National Stock Number;United Nations Standard Products and Services Code;Pricing Action\n")
        csv_file.write(
            "feed_product_type;item_sku;brand_name;external_product_id;external_product_id_type;item_name;recommended_browse_nodes;outer_material_type;material_composition;color_map;color_name;size_name;department_name;size_map;is_adult_product;standard_price;quantity;main_image_url;other_image_url1;other_image_url2;other_image_url3;other_image_url4;other_image_url5;other_image_url6;other_image_url7;other_image_url8;parent_child;parent_sku;relationship_type;variation_theme;update_delete;product_description;inner_material_type;care_instructions;model_name;model;part_number;gtin_exemption_reason;generic_keywords;collection_name;pattern_type;lifestyle;fit_type;bullet_point1;bullet_point2;bullet_point3;bullet_point4;bullet_point5;platinum_keywords1;platinum_keywords2;platinum_keywords3;platinum_keywords4;platinum_keywords5;seasons;material_type;style_name;sleeve_type;collar_style;special_size_type;neck_size;neck_size_unit_of_measure;website_shipping_weight;website_shipping_weight_unit_of_measure;item_width;item_height;item_shape;item_dimensions_unit_of_measure;item_length;fulfillment_center_id;package_length;package_width;package_height;package_weight;package_weight_unit_of_measure;package_dimensions_unit_of_measure;legal_disclaimer_description;safety_warning;eu_toys_safety_directive_age_warning;eu_toys_safety_directive_warning;eu_toys_safety_directive_language;country_of_origin;batteries_required;are_batteries_included;battery_cell_composition;battery_type1;battery_type2;battery_type3;number_of_batteries1;number_of_batteries2;number_of_batteries3;battery_weight;battery_weight_unit_of_measure;number_of_lithium_metal_cells;number_of_lithium_ion_cells;lithium_battery_packaging;lithium_battery_energy_content;lithium_battery_energy_content_unit_of_measure;lithium_battery_weight;lithium_battery_weight_unit_of_measure;supplier_declared_dg_hz_regulation1;supplier_declared_dg_hz_regulation2;supplier_declared_dg_hz_regulation3;supplier_declared_dg_hz_regulation4;supplier_declared_dg_hz_regulation5;hazmat_united_nations_regulatory_id;safety_data_sheet_url;item_weight;item_weight_unit_of_measure;item_volume;item_volume_unit_of_measure;flash_point;ghs_classification_class1;ghs_classification_class2;ghs_classification_class3;condition_type;condition_note;currency;fulfillment_latency;sale_price;sale_from_date;sale_end_date;max_aggregate_ship_quantity;item_package_quantity;number_of_items;offering_can_be_gift_messaged;offering_can_be_giftwrapped;is_discontinued_by_manufacturer;product_site_launch_date;restock_date;list_price;offering_end_date;max_order_quantity;merchant_shipping_group_name;offering_start_date;delivery_schedule_group_id;uvp_list_price;product_tax_code;business_price;quantity_price_type;quantity_lower_bound1;quantity_price1;quantity_lower_bound2;quantity_price2;quantity_lower_bound3;quantity_price3;quantity_lower_bound4;quantity_price4;quantity_lower_bound5;quantity_price5;national_stock_number;unspsc_code;pricing_action\n")
        csv_file.write("\n\n")
        csv_file.close()


def test_data():
    product_names = ["UK", "DE", "FR", "IT", "ES"]
    browser_nodes = ["UK", "DE", "FR", "IT", "ES"]
    bullet_points = ["UK;UK;UK;UK;UK;", "DE;DE;DE;DE;DE;", "FR;FR;FR;FR;FR;", "IT;IT;IT;IT;IT;", "ES;ES;ES;ES;ES;"]
    add_to_excel("Produck_type", "1091 Seller_SKU", "Brand_name", product_names, browser_nodes, "meterial_comp",
                 "color_map", "department", "price", "dropbox_url", "other_image_url", bullet_points)


def add_to_excel(produck_type, seller_SKU, brand_name, product_names, browser_nodes, meterial_comp, color_map,
                 department, price, dropbox_url, other_image_url, bullet_points):
    sizes = [" parent", " S", " M", " L", " XL", " XXL"]
    size_name = ["", "S", "M", "L", "XL", "XXL"]
    size_map = ["", " Small", " Medium", " Large", " X-Large", " XX-Large"]
    file_names = ["UK", "DE", "FR", "IT", "ES"]
    parent_child = ["Parent", "Child", "Child", "Child", "Child", "Child"]
    parent_sku = ["", seller_SKU + " parent", seller_SKU + " parent", seller_SKU + " parent",
                  seller_SKU + " parent", seller_SKU + " parent"]
    relationship = ["", "Variation", "Variation", "Variation", "Variation", "Variation", ]
    collection_name = ["Spring-Summer 12", "Spring-Summer 13", "Spring-Summer 14", "Spring-Summer 15",
                       "Spring-Summer 16", "Spring-Summer 17"]
    currency = ["GBP", "EUR", "EUR", "EUR", "EUR"]
    for f, file_name in enumerate(file_names):
        csv_file = open(file_name + ".csv", "a")
        for s, size in enumerate(sizes):
            csv_file.write(produck_type + ";" + seller_SKU + size + ";" + brand_name + ";;GTIN;" + product_names[f] +
                           ";" + browser_nodes[
                               f] + ";Cotton;" + meterial_comp + ";" + color_map + ";" + color_map + ";" +
                           size_name[s] + ";" + department + ";" + size_map[s] + ";FALSE;" + price + ";5000;" +
                           dropbox_url + ";" + other_image_url + ";;;;;;;;" + parent_child[s] + ";" + parent_sku[s]
                           + ";" + relationship[s] + ";Size;;;;;;;;;" + product_names[f] + ";" +
                           collection_name[s] + ";;Casual;Regular Fit;" + bullet_points[f] +
                           ";;;;;;Spring-Summer;Cotton;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;" +
                           currency[f] + "\n")
        csv_file.write("\n")
        csv_file.close()


def test():
    # noinspection PyBroadException
    try:
        create()
    except:
        messagebox.showwarning("Warning", "Files already exists, please remove them to create a new ones.")
    test_data()
    CsvToXlsx.convert_all()
