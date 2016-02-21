float _puw_Mu8[60] = { 1.0, 0.9994454279492937, 1.1408730062090167, 1.1896895249584971, 1.1811747508002342, 1.1726109230504829, 1.1583169618422073, 1.12784866887298, 1.1168934226540446, 1.0802089151662735, 1.0102211008885693, 0.9814562995802677, 0.9240760711877053, 0.8795489035808324, 0.8561616190703987, 0.8266394017063057, 0.7563068028440882, 0.6928551845526816, 0.6630149804023878, 0.6059242279752675, 0.6315038426526468, 0.4491181183881366, 0.37351101394494163, 0.2771058410560153, 0.2630938492888388, 0.27709712339040293, 0.33813514662832367, 0.11780751636474518, 0.20677172919356485, 0.18476488894115173, 0.13478610600871918, 1.0, 0.2611146605629049, 0.4735661703304179, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };
float _puw_Mu17[60] = { 1.0, 0.8747565142376306, 1.0743016948119088, 1.1116791559127828, 1.1426720757503066, 1.1595949353869266, 1.1483393816557843, 1.1278430019523449, 1.1025601606619817, 1.0753427320894413, 1.0373488436884102, 0.9863229923805926, 0.9516751257389059, 0.9058234353250314, 0.8600405760305825, 0.8034008870738618, 0.7703276554023905, 0.7142014716044455, 0.6712220307924187, 0.6070894063589435, 0.5502250459798711, 0.5273158187520325, 0.4166135475763699, 0.3701387235448416, 0.33003691310889666, 0.22304764557292248, 0.17520327746866135, 0.1360714347832837, 0.1118889360771643, 0.08304831768538007, 0.03139731654549161, 0.08780475451923876, 0.019039681951079336, 0.022752474197740902, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };

float _puw_Ele12_CaloIdM_TrackIdM_PFJet30[60] = { 1.0, 0.8666718532462329, 0.9678137861162525, 1.0393069911397503, 1.1388006009299214, 1.06660404634288, 1.0926550729113051, 1.0676667529856092, 1.096422969980387, 1.0363228625987242, 1.0387343922480008, 0.9905074701186719, 0.9807342334173867, 0.9358715250119044, 0.8558293849764206, 0.845087669289883, 0.8756376558677058, 0.7547154651757071, 0.7143783220375851, 0.7180693248368629, 0.6061415066619141, 0.6660333134867166, 0.4535427844116779, 0.3823597874923331, 0.33470305810407364, 0.20478291805305784, 0.39135448565880426, 0.06972460182375562, 0.02882982563505961, 0.1568969813302214, 0.05205859733762233, 0.1148992595255287, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 };

float _puw_Z3l[60] = { 1.0001741265822783, 3.2730109160906333, 2.010298357298091, 0.5454273123981134, 1.311685758741014, 0.9453760849229369, 1.485991355696928, 1.0576276129864648, 1.04220293323621, 1.0194351137699198, 0.9046037505579173, 0.9735784748126046, 0.9400994953706878, 1.0640732793280163, 0.9021651383805767, 0.9605763679547218, 0.6890592129508076, 0.8633128475449122, 0.727349614999339, 0.4654128362542978, 1.8124654834695133, 0.6156354166193685, 0.5015015429027262, 0.0, 0.9730616716126524, 0.0, 0.0, 0.0, 0.0, 1.0001741265822783, 0.0, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 0.0, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783, 1.0001741265822783 };

float puwMu8(int nVert) { return _puw_Mu8[nVert] * (82457.0/161885395.263); }
float puwMu17(int nVert) { return _puw_Mu17[nVert] * (1980317.0/26859995.3357); }
float puwEle12_CaloIdM_TrackIdM_PFJet30(int nVert) { return _puw_Ele12_CaloIdM_TrackIdM_PFJet30[nVert] * (303982.0/62188555.3882); }
float puwZ3l(int nVert) { return _puw_Z3l[nVert]; }


void frPuReweight() {}
