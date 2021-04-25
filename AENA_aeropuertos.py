#!/usr/bin/env python
# coding: utf-8

# In[40]:


aeropuertos = {}

aeropuertos["MAD"] = {}
aeropuertos["MAD"]["Nombre"] = "ADOLFO SUÁREZ MADRID-BARAJAS"
aeropuertos["MAD"]["Otros"] = ["ADOLFO SUAREZ MADRID-BARAJAS", "MADRID-BARAJAS"]

aeropuertos["ZAZ"] = {}
aeropuertos["ZAZ"]["Nombre"] = "ZARAGOZA"

aeropuertos["BCN"] = {}
aeropuertos["BCN"]["Nombre"] = "JOSEP TARRADELLAS BARCELONA-EL PRAT"
aeropuertos["BCN"]["Otros"] = ["BARCELONA-EL PRAT J.T.", "BARCELONA-EL PRAT", "BARCELONA"]

aeropuertos["VIT"] = {}
aeropuertos["VIT"]["Nombre"] = "VITORIA"

aeropuertos["LPA"] = {}
aeropuertos["LPA"]["Nombre"] = "GRAN CANARIA"

aeropuertos["VLC"] = {}
aeropuertos["VLC"]["Nombre"] = "VALENCIA"

aeropuertos["SVQ"] = {}
aeropuertos["SVQ"]["Nombre"] = "SEVILLA"

aeropuertos["TFN"] = {}
aeropuertos["TFN"]["Nombre"] = "TENERIFE NORTE-CIUDAD DE LA LAGUNA"
aeropuertos["TFN"]["Otros"] = ["TENERIFE NORTE-C. LA LAGUNA", "TENERIFE NORTE", "TENERIFE-NORTE"]

aeropuertos["PMI"] = {}
aeropuertos["PMI"]["Nombre"] = "PALMA DE MALLORCA"

aeropuertos["SCQ"] = {}
aeropuertos["SCQ"]["Nombre"] = "SANTIAGO-ROSALÍA DE CASTRO"
aeropuertos["SCQ"]["Otros"] = ["SANTIAGO", "SANTIAGO-ROSALIA DE CASTRO"]

aeropuertos["ALC"] = {}
aeropuertos["ALC"]["Nombre"] = "ALICANTE-ELCHE"
aeropuertos["ALC"]["Otros"] = ["ALICANTE"]

aeropuertos["MAH"] = {}
aeropuertos["MAH"]["Nombre"] = "MENORCA"

aeropuertos["AGP"] = {}
aeropuertos["AGP"]["Nombre"] = "MÁLAGA-COSTA DEL SOL"
aeropuertos["AGP"]["Otros"] = ["MÁLAGA", "MALAGA", "MALAGA-COSTA DEL SOL"]

aeropuertos["IBZ"] = {}
aeropuertos["IBZ"]["Nombre"] = "IBIZA"

aeropuertos["TFS"] = {}
aeropuertos["TFS"]["Nombre"] = "TENERIFE SUR"
aeropuertos["TFS"]["Otros"] = ["TENERIFE-SUR"]

aeropuertos["ACE"] = {}
aeropuertos["ACE"]["Nombre"] = "CÉSAR MANRIQUE-LANZAROTE"
aeropuertos["ACE"]["Otros"] = ["LANZAROTE CÉSAR MANRIQUE", "LANZAROTE CESAR MANRIQUE","LANZAROTE"]

aeropuertos["VGO"] = {}
aeropuertos["VGO"]["Nombre"] = "VIGO"

aeropuertos["FUE"] = {}
aeropuertos["FUE"]["Nombre"] = "FUERTEVENTURA"

aeropuertos["SPC"] = {}
aeropuertos["SPC"]["Nombre"] = "LA PALMA"

aeropuertos["BIO"] = {}
aeropuertos["BIO"]["Nombre"] = "BILBAO"

aeropuertos["GRO"] = {}
aeropuertos["GRO"]["Nombre"] = "GIRONA-COSTA BRAVA"
aeropuertos["GRO"]["Otros"] = ["GIRONA"]

aeropuertos["VDE"] = {}
aeropuertos["VDE"]["Nombre"] = "EL HIERRO"

aeropuertos["LCG"] = {}
aeropuertos["LCG"]["Nombre"] = "A CORUÑA"

aeropuertos["OVD"] = {}
aeropuertos["OVD"]["Nombre"] = "ASTURIAS"

aeropuertos["MLN"] = {}
aeropuertos["MLN"]["Nombre"] = "MELILLA"

aeropuertos["GMZ"] = {}
aeropuertos["GMZ"]["Nombre"] = "LA GOMERA"

aeropuertos["RMU"] = {}
aeropuertos["RMU"]["Nombre"] = "INTERNACIONAL REGIÓN DE MURCIA"
aeropuertos["RMU"]["Otros"] = ["MURCIA", "AEROPUERTO INTL. REGIÓN MURCIA", "AEROPUERTO INTL. REGIÓN MURCIA (**)", "AEROPUERTO INTL. REGIÓN MURCIA  (**)"]

aeropuertos["ABC"] = {}
aeropuertos["ABC"]["Nombre"] = "ALBACETE"
aeropuertos["ABC"]["Otros"] = ["ALBACETE-LOS LLANOS", "ALBACETE LOS LLANOS"]

aeropuertos["AEI"] = {}
aeropuertos["AEI"]["Nombre"] = "ALGECIRAS"
aeropuertos["AEI"]["Otros"] = ["ALGECIRAS-HELIPUERTO", "ALGECIRAS /HELIPUERTO"]

aeropuertos["LEI"] = {}
aeropuertos["LEI"]["Nombre"] = "ALMERÍA"
aeropuertos["AEI"]["Otros"] = ["ALMERIA"]

aeropuertos["BJZ"] = {}
aeropuertos["BJZ"]["Nombre"] = "BADAJOZ"

aeropuertos["RGS"] = {}
aeropuertos["RGS"]["Nombre"] = "BURGOS"

aeropuertos["ODB"] = {}
aeropuertos["ODB"]["Nombre"] = "CÓRDOBA"
aeropuertos["ODB"]["Otros"] = ["CORDOBA"]

aeropuertos["JCU"] = {}
aeropuertos["JCU"]["Nombre"] = "CEUTA"
aeropuertos["JCU"]["Otros"] = ["CEUTA-HELIPUERTO", "CEUTA /HELIPUERTO"]

aeropuertos["GRX"] = {}
aeropuertos["GRX"]["Nombre"] = "FEDERICO GARCÍA LORCA GRANADA-JAÉN"
aeropuertos["GRX"]["Otros"] = ["FEDERICO GARCIA LORCA GRANADA-JAÉN", "FEDERICO GARCÍA LORCA GRANADA-JAEN","FEDERICO GARCIA LORCA GRANADA-JAEN","FGL GRANADA-JAEN","FGL GRANADA-JAÉN","F.G.L. GRANADA-JAEN","F.G.L. GRANADA-JAÉN", "GRANADA"]

aeropuertos["HSK"] = {}
aeropuertos["HSK"]["Nombre"] = "HUESCA-PIRINEOS"
aeropuertos["HSK"]["Otros"] = ["HUESCA PIRINEOS", "HUESCA"]

aeropuertos["XRY"] = {}
aeropuertos["XRY"]["Nombre"] = "JEREZ"
aeropuertos["XRY"]["Otros"] = ["JEREZ DE LA FRONTERA"]

aeropuertos["LEN"] = {}
aeropuertos["LEN"]["Nombre"] = "LEÓN"
aeropuertos["LEN"]["Otros"] = ["LEON"]

aeropuertos["RJL"] = {}
aeropuertos["RJL"]["Nombre"] = "LOGROÑO-AGONCILLO"
aeropuertos["LEN"]["Otros"] = ["LOGROÑO"]

aeropuertos["PNA"] = {}
aeropuertos["PNA"]["Nombre"] = "PAMPLONA"

aeropuertos["REU"] = {}
aeropuertos["REU"]["Nombre"] = "REUS"

aeropuertos["QSA"] = {}
aeropuertos["QSA"]["Nombre"] = "SABADELL"

aeropuertos["SLM"] = {}
aeropuertos["SLM"]["Nombre"] = "SALAMANCA"

aeropuertos["EAS"] = {}
aeropuertos["EAS"]["Nombre"] = "SAN SEBASTIÁN"
aeropuertos["EAS"]["Otros"] = ["SAN SEBASTIAN"]

aeropuertos["LECU"] = {}
aeropuertos["LECU"]["Nombre"] = "MADRID-CUATRO VIENTOS"
aeropuertos["LECU"]["Otros"] = ["MADRID CUATRO VIENTOS"]

aeropuertos["SDR"] = {}
aeropuertos["SDR"]["Nombre"] = "SEVE BALLESTEROS-SANTANDER"
aeropuertos["SDR"]["Otros"] = ["SANTANDER"]

aeropuertos["LESB"] = {}
aeropuertos["LESB"]["Nombre"] = "SON BONET"

aeropuertos["VLL"] = {}
aeropuertos["VLL"]["Nombre"] = "VALLADOLID"

aeropuertos["MJV"] = {}
aeropuertos["MJV"]["Nombre"] = "MURCIA-SAN JAVIER"
aeropuertos["MJV"]["Otros"] = ["MURCIA-SAN JAVIER  (*)", "MURCIA SAN JAVIER"]

aeropuertos["TOJ"] = {}
aeropuertos["TOJ"]["Nombre"] = "MADRID-TORREJÓN"
aeropuertos["TOJ"]["Otros"] = ["MADRID-TORREJON", "ADRID TORREJON"]


# In[41]:





# In[ ]:





# In[ ]:




