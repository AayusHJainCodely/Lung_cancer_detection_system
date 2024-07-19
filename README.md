# Lung_cancer_detection_system
## Introduction
Cancer has become one of the most persistent diseases to arise over the past century, presenting significant challenges for healthcare professionals, particularly in ensuring early detection. The ability to pinpoint cancer biomarkers at a molecular level is pivotal in achieving timely diagnosis, setting the stage for tailored and efficacious treatment strategies.By integrating biological recognition elements with electronic transducers, transistor-based biosensors can provide rapid and accurate detection, which is essential for early diagnosis.

## Detection of CYFRA 21-1
Cytokeratin fragment 21-1,crucial tumor marker to detect whether diagnosis is for small or non-small lung cancer.

In fabrication SiO2 surface modified with APTES SAM and cross-linker glutaraldehyde to facilitate immobilization of anti-CYFRA antibodies. The surface was washed with 0.01× PBS to remove any residue and then treated with BSA to block non-specific adsorption and enhance the sensor’s specificity for CYFRA 21-1.

## Detection of NSE
Neuron-specific enolase (NSE) serves as a vital biomarker in the diagnosis of various cancers, including lung cancer, due to its association with neuronal and neuroendocrine tissues. The NSE detection, using multianalyte FET biosensor.
The SiO2 surface was modified with APTES SAM and cross-linker glutaraldehyde (GA) to facilitate the immobilization of anti-NSE antibodies, followed by washing with 0.01× PBS and blocking with BSA to enhance specificity. Electrical measurements were conducted to detect NSE-specific changes on the gate surface, demonstrating the biosen sor’s sensitivity and accuracy in detecting NSE in both PBS and human serum samples. Another biosensor for the detection of Neuron-Specific Enolase (NSE), a biomarker associated with lung cancer, was fabricated using a tailored approach. The fabrication process specifically focused on enhancing the mobility and ultrasensitivity of the organic electrochemical transistors (OECTs) device for NSE detection. Silver nanowires (AgNWs) were doped into the organic semiconductor, PEDOT: PSS, to improve electronic mobility and facilitate the ion-electron transfer process crucial for amplifying small NSE signals. The integration of AgNWs-doped OECTs biosensors aimed to recover the ion/electron transport process in sputum samples, enabling the ultrasensitive detection of NSE down to pg/mL levels. The NSE biosensor was designed to be part of a multiplexed, miniaturized 

## Detection of CEA
Carcinoembroygenic antigen 
Effect Transistor (FET) design, integrating a semiconducting carbon nanotube (CNT) film with an undulating yttrium oxide (Y2O3) dielectric layer at the biosensing interface. The sensor fabrication involves engineering the undulating Y2O3 layer to create an optimal biosensing surface for probe immobilization, optimizing the CNT-FET biosensor’s performance. With an enlarged gate area, the sensor achieves remarkable sensitivity, detecting CEA at levels as low as 72 ag/mL in phosphate-buffered saline (PBS) and 155 ag/mL in fetal bovine serum (FBS). Another biosensor for carcinoembryonic antigen (CEA) detection, the CNT-doped transition metal carbide-based organic electrochemical transistor (CM-OECAT). In the fabrication of the CNT-doped transition metal carbide-based organic electrochemical tran sistor (CM-OECAT) for carcinoembryonic antigen (CEA) detection, meticulous steps were taken to enhance the sensor’s semiconductor performance. This involved incorporating carbon nanotubes into MXene material, followed by de tailed characterization of the morphology through microscopy analysis. The synthesis process included sodium hydroxide etching of transition metal carbides to obtain MX ene with a unique layered structure, and a hydrothermal method to combine CNT with MXene, as confirmed by SEM and electron diffraction analysis.
## Detection of miR-21
MicroRNA-21 (miR-21), a vital lung cancer biomarker, was targeted for detection using a semiconducting silicon nanowire field-effect transistor (SiNW-FET) biosensor array. Fab rication involved optical lithography and anisotropic self-stop etching for cost-effective production of precise silicon nanowires. Through pH sensing experiments, optimal work ing conditions were established, enabling the sensor to detect miR-21 at 1 fM concentra tions with exceptional sensitivity and specificity, crucial for early cancer diagnosis. Another biosensor for the detection of the lung cancer biomarker miR-21 was fabri cated using a nanoflower-shaped MXene-based field-effect transistor (NSMXFETs). The fabrication process involved modifying the electrodes with miR-21 aptamer, confirming specificity through SEM imaging, and ensuring exclusion of interference substances like miR-31. Characterization of the NSMXFETs included SEM imaging to analyze the dis tribution of elements such as Mn, Al, and C on the two-dimensional morphology.

## Data transfer and processing
### COMMUNICATION PROTOCOLS
The three most common protocols:Serial Peripheral Interface (SPI),Inter-Integrated Circuit (I2C),Universal Asynchronous Receiver/Transmitter (UART) driven communication.
#### I2C protocol
I2C is a serial communication protocol,data is transferred bit by bit along a single wire (the SDA
line).With I2C, data is transferred in messages.Messages are broken up into frames of data.Each message has an address frame that contains the binary address of the slave, and one or more data frames that contain the data being transmitted.
The message also includes start and stop conditions, read/write bits, and ACK/NACK bits between each data frame.
#### Reading the temperature and Humidity values from Raspberry pi
The raw data is collected  from the sensors and displayed   on the terminal of the pi4 to just check the values of the sensors.
Prerequisite :- Make sure I2C AND GPIO are enabled from your raspberry pi configuration


Step 1 : - Install the library for htu21d and dht11 using following command

pip install adafruit-circuitpython-htu21d adafruit-circuitpython-dht

Step 2 :- Create a file name example sensors.py to do that use following command

nano sensors.py
step:-Run the file uing command
python sensors.py
### Giving Vgs(biasing voltage) through pi and reading Igs values
The MCP4725 is a 12-bit Digital-to-Analog Converter (DAC) with non-volatile memory and 12-bit resolution. It provides a simple and cost-effective solution for converting digital signals from a microcontroller or other digital sources into analog voltages with a wide range of 2.7 to 5.5V.It is compatible with I2C interface.

Implemented a system where two distinct voltage levels are being applied across IRF540 ,a N-type MOSFET. This particular
MOSFET is comprised of P-type material called as substrate and contains two N-type impurities that are configured as the
source and drain.
In this arrangement, the source operates analogously to the emitter in a traditional transistor, while the drain fulfills a
comparable role to the collector. The gate, in this specific context, can be likened to the base of a transistor.
Given the prevalence of the common emitter configuration in transistor applications, we adhere to this configuration and
ground the source. Subsequently, we provide a gate-source voltage that is lower than the gate-drain voltage through the use
of a DAC (digital-to-analog converter). This setup facilitates adjustments to the voltage values based on user inputs, which are
integrated into the system via a Raspberry Pi.


