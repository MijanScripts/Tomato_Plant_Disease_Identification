#Import libraries
import streamlit as st
import numpy as np
import cv2
from  PIL import Image, ImageEnhance

option = st.selectbox(
     'Tomato diseases',
     ('Tomato Yellow Leaf Curl disease', 'Tomato mosaic virus', 'Tomato Early blight', 'Tomato Leaf Mold', 'Tomato Septoria leaf spot','Tomato Target Spot','Tomato Bacterial Spot','Tomato Late Blight','Tomato Spider mites (Two-spotted spider mite)'))

if option == 'Tomato Yellow Leaf Curl disease':
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.header('Tomato Yellow Leaf Curl disease')
        image1 = Image.open('CNN_Model/Tomatoes/Tomato___Tomato_Yellow_Leaf_Curl_Virus/0a0fe942-bb9e-4384-8466-779017d00bcf___UF.GRC_YLCV_Lab 02192.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/Tomato___Tomato_Yellow_Leaf_Curl_Virus/8b16cc37-30cc-4685-a5fd-6259d200451a___YLCV_NREC 2270.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('The infected leaves become reduced in size, curl upward, appear crumpled and show yellowing of veins and leaf margins. The internodes become shorter and the whole plant appears stunted and bushy. The whole plant stands erect with only upright growth. The flowers may not develop and drop off.')
        st.subheader('Cause')
        st.write('Virus (family Geminiviridae, genus Begomovirus)')
    with col3:
        st.subheader('Observation')
        st.write('The virus is transmitted by white flies and may cause 100 % yield loss if the plants infect at an early stage of crop. The virus also infect other hosts like common beans, ornamental plants and several weed species.')
        st.subheader('Control')
        st.write('Grow available resistant varieties. Transplant only disease and whiteflies free seedlings. Remove the infected plants and burn them. Keep the field free from weeds. Use yellow sticky traps to monitor and control whiteflies. If the insect infestation is severe, spray suitable insecticides.')

if option == 'Tomato mosaic virus':
    col1, col2, col3 = st.columns( [1, 1, 1])
    with col1:
        st.header('Tomato mosaic virus')
        image1 = Image.open('CNN_Model/Tomatoes/Tomato___Tomato_mosaic_virus/4ab92098-cb26-40ef-b145-fbd1cdde9bd5___PSU_CG 2392.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/Tomato___Tomato_mosaic_virus/bd22aa4a-ea90-41af-862d-7e887eb57a00___PSU_CG 2416.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('Symptoms can occur at any growth stage and any part of the plant can be affected; infected leaves generally exhibit a dark green mottling or mosaic; some strains of the virus can cause yellow mottling on the leaves; young leaves may be stunted or distorted; severely infected leaves may have raised green areas; fruit yields are reduced in infected plants; green fruit may have yellow blotches or necrotic spots; dark necrotic streaks may appear on the stems, petioles leaves and fruit.')
        st.subheader('Cause')
        st.write('Virus (Tomato mosaic virus (ToMV)')
    with col3:
        st.subheader('Observation')
        st.write('ToMV is a closely related strain of Tobacco mosaic virus (TMV), it enters fields via infected weeds, peppers or potato plants; the virus may also be transmitted to tomato fields by grasshoppers, small mammals and birds.')
        st.subheader('Control')
        st.write('Plant varieties that are resistant to the virus; heat treating seeds at 70°C (158°F) for 4 days or at 82–85°C (179.6–185°F) for 24 hours will help to eliminate any virus particles on the surface of the seeds; soaking seed for 15 min in 100 g/l of tri-sodium phosphate solution (TSP) can also eliminate virus particles - seeds should be rinsed thoroughly and laid out to dry after this treatment; if the virus is confirmed in the field, infected plants should be removed and destroyed to limit further spread; plant tomato on a 2-year rotation, avoiding susceptible crops such as peppers, eggplant, cucurbits and tobacco; disinfect all equipment when moving from infected areas of the field.')

if option == 'Tomato Early blight':
    col1, col2, col3 = st.columns( [1, 1, 1])
    with col1:
        st.header('Tomato Early blight')
        image1 = Image.open('CNN_Model/Tomatoes/Tomato___Early_blight/0abc57ec-7f3b-482a-8579-21f3b2fb780b___RS_Erly.B 7609.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/Tomato___Early_blight/0db67be3-f733-4d15-b7d9-5d075b2cafc7___RS_Erly.B 6401.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('Early blight symptoms start as oval-shaped lesions with a yellow chlorotic region across the lesion; concentric leaf lesions may be seen on infected leaves; leaf tissue between veins is destroyed; severe infections can cause leaves to completely collapse; as the disease progresses leaves become severely blighted leading to reduced yield.')
        st.subheader('Cause')
        st.write('Fungus( Alternaria solani)')
    with col3:
        st.subheader('Observation')
        st.write('The disease can spread rapidly after plants have set fruit; movement of air-borne spores and contact with infested soil are causes for the spread of the disease.')
        st.subheader('Control')
        st.write('Apply appropriate fungicide at the first sign of disease; destroy any volunteer solanaceous plants (tomato, potato, nightshade, etc); practice crop rotation.')

if option == 'Tomato Septoria leaf spot':
    col1, col2, col3 = st.columns( [1, 1, 1])
    with col1:
        st.header('Tomato Septoria leaf spot')
        image1 = Image.open('CNN_Model/Tomatoes/Tomato___Septoria_leaf_spot/0a5edec2-e297-4a25-86fc-78f03772c100___JR_Sept.L.S 8468.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/Tomato___Septoria_leaf_spot/0b23b869-cfa6-40d7-a683-f4637d91ebff___Matt.S_CG 1286.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('Symptoms may occur at any stage of tomato development and begin as small, water-soaked spots or circular grayish-white spots on the underside of older leaves; spots have a grayish center and a dark margin and they may coalesce; fungal fruiting bodies are visible as tiny black specks in the center of spot; spots may also appear on stems, fruit calyxes, and flowers.')
        st.subheader('Cause')
        st.write('Fungus(Septoria lycopersici)')
    with col3:
        st.subheader('Observation')
        st.write('Spread by water splash; fungus overwinters in plant debris.')
        st.subheader('Control')
        st.write('Ensure all tomato crop debris is removed and destroyed in Fall or plowed deep into the soil; plant only disease-free material; avoid overhead irrigation; stake plants to increase air circulation through the foliage; apply appropriate fungicide if necessary.')

if option == 'Tomato Target Spot':
    col1, col2, col3 = st.columns( [1, 1, 1])
    with col1:
        st.header('Tomato Target Spot')
        image1 = Image.open('CNN_Model/Tomatoes/Tomato___Target_Spot/0cb83b4d-281d-4b8f-a52a-8178fa8af907___Com.G_TgS_FL 7928.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/Tomato___Target_Spot/64d22974-a348-47f8-811b-f68c58963c36___Com.G_TgS_FL 7887.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('The fungus infects all parts of the plant. Infected leaves show small, pinpoint, water soaked spots initially. As the disease progresses the spots enlarge to become necrotic lesions with conspicuous concentric circles, dark margins and light brown centers. Whereas the fruits exhibit brown, slightly sunken flecks in the beginning but later the lesions become large pitted appearance.')
        st.subheader('Cause')
        st.write('Fungus (Corynespora cassiicola)')
    with col3:
        st.subheader('Observation')
        st.write('The pathogen infects cucumber, pawpaw , ornamental plants, some weed species etc. The damaged fruits are susceptible to this disease.')
        st.subheader('Control')
        st.write('Remove the plant debris and burn them. Avoid over application of nitrogen fertilizer. If the disease is severe, spray suitable fungicides.')

if option == 'Tomato Bacterial Spot':
    col1, col2, col3 = st.columns( [1, 1, 1])
    with col1:
        st.header('Tomato Bacterial Spot')
        image1 = Image.open('CNN_Model/Tomatoes/train/tomatoes_Bacterial_spot/40688c11-791b-465a-9476-a5069e24a56f___GCREC_Bact.Sp 3064.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/train/tomatoes_Bacterial_spot/79466870-1413-4b75-93e6-31b827cfa3ac___GCREC_Bact.Sp 6043.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('Bacterial spot lesions starts out as small water-soaked spots; lesions become more numerous and coalesce to form necrotic areas on the leaves giving them a blighted appearance; of leaves drop from the plant severe defoliation can occur leaving the fruit susceptible to sunscald; mature spots have a greasy appearance and may appear transparent when held up to light; centers of lesions dry up and fall out of the leaf; blighted leaves often remain attached to the plant and give it a blighted appearance.')
        st.subheader('Cause')
        st.write('Bacterium (Xanthomonas)')
    with col3:
        st.subheader('Observation')
        st.write('Bacteria survive on crop debris; disease emergence favored by warm temperatures and wet weather; symptoms are very similar to other tomato diseases but only bacterial spot will cause a cut leaf to ooze bacterial exudate; the disease is spread by infected seed, wind-driven rain, diseased transplants, or infested soil; bacteria enter the plant through any natural openings on the leaves or any openings caused by injury to the leaves.')
        st.subheader('Control')
        st.write('Use only certified seed and healthy transplants; remove all crop debris from the planting area; do not use sprinkler irrigation, instead water from the base of the plant; rotate crops.')

if option == 'Tomato Late Blight':
    col1, col2, col3 = st.columns( [1, 1, 1])
    with col1:
        st.header('Tomato Late Blight')
        image1 = Image.open('CNN_Model/Tomatoes/Tomato___Late_blight/0a4b3cde-c83a-4c83-b037-010369738152___RS_Late.B 6985.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/Tomato___Late_blight/0b33d7a7-d017-4857-845a-874a004ccd26___RS_Late.B 4970.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('Late blight affects all aerial parts of the tomato plant; initial symptoms of the disease appear as water-soaked green to black areas on leaves which rapidly change to brown lesions; fluffy white fungal growth may appear on infected areas and leaf undersides during wet weather; as the disease progresses, foliage becomes becomes shriveled and brown and the entire plant may die; fruit lesions start as irregularly shaped water soaked regions and change to greasy spots; entire fruit may become infected and a white fuzzy growth may appear during wet weather.')
        st.subheader('Cause')
        st.write('Oomycete (Phytophthora infestans)')
    with col3:
        st.subheader('Observation')
        st.write('Can devastate tomato plantings.')
        st.subheader('Control')
        st.write('Plant resistant varieties; if signs of disease are present or if rainy conditions are likely or if using overhead irrigation appropriate fungicides should be applied.')

if option == 'Tomato Spider mites (Two-spotted spider mite)':
    col1, col2, col3 = st.columns( [1, 1, 1])
    with col1:
        st.header('Tomato Spider mites (Two-spotted spider mite)')
        image1 = Image.open('CNN_Model/Tomatoes/Tomato___Spider_mites Two-spotted_spider_mite/3ba4c514-567a-4e4b-9d22-9cf2a957e906___Com.G_SpM_FL 1198.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/Tomato___Spider_mites Two-spotted_spider_mite/0a714292-45d6-483a-bbd0-2eab8fe72888___Com.G_SpM_FL 1496.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('Leaves stippled with yellow; leaves may appear bronzed; webbing covering leaves; mites may be visible as tiny moving dots on the webs or underside of leaves, best viewed using a hand lens; usually not spotted until there are visible symptoms on the plant; leaves turn yellow and may drop from plant.')
        st.subheader('Cause')
        st.write('Arachnid (Tetranychus urticae)')
    with col3:
        st.subheader('Observation')
        st.write('Spider mites thrive in dusty conditions; water-stressed plants are more susceptible to attack.')
        st.subheader('Control')
        st.write('In the home garden, spraying plants with a strong jet of water can help reduce buildup of spider mite populations; if mites become problematic apply insecticidal soap to plants; certain chemical insecticides may actually increase mite populations by killing off natural enemies and promoting mite reproduction.')

if option == 'Tomato Leaf Mold':
    col1, col2, col3 = st.columns( [1, 1, 1])
    with col1:
        st.header('Tomato Leaf Mold')
        image1 = Image.open('CNN_Model/Tomatoes/Tomato___Leaf_Mold/0a9b3ff4-5343-4814-ac2c-fdb3613d4e4d___Crnl_L.Mold 6559.JPG')
        image2 = Image.open('CNN_Model/Tomatoes/Tomato___Leaf_Mold/9445a483-85a6-465c-b9b0-1ff8bc519a43___Crnl_L.Mold 9035.JPG')
        st.image(image1)
        st.image(image2)
    with col2:
        st.subheader('Symptoms')
        st.write('The older leaves exhibit pale greenish to yellow spots on the upper surface. Whereas the lower portion of these spots exhibits green to brown velvety fungal growth. As the disease progresses the spots may coalesce and appear brown. The infected leaves become wither and die but stay attached to the plant. The fungus also infects flowers and fruits. The affected flowers become black and drop off. The affected fruit initially shows smooth black irregular area on the stem end but later it becomes sunken, leathery, and dry.')
        st.subheader('Cause')
        st.write('Fungus (Passalora fulva)')
    with col3:
        st.subheader('Observation')
        st.write('The disease is favored by high relative humidity. Also a common disease in greenhouse tomato crops.')
        st.subheader('Control')
        st.write('Grow available resistant varieties. Avoid leaf wetting and overhead application of water. Follow proper spacing to provide good air circulation around the plants. Remove the infected plant debris and burn them. If the disease is severe, scary suitable fungicide.')
