
# Parameters and results of model training
<table>
    <thead>
        <tr>
            <td rowspan=2 align="center">name</td>
            <td rowspan=2 align="center">model</td>
            <td rowspan=2 align="center">epochs</td>
            <td rowspan=2 align="center">GFLOps</td>
            <td rowspan=2 align="center">imgsz</td>
            <td rowspan=2 align="center">train</td>
            <td rowspan=2 align="center">val</td>
            <td rowspan=2 align="center">val / train</td>
            <td colspan=2 align="center">precision</td>
            <td colspan=2 align="center">recall</td>
            <td colspan=2 align="center">mAP50</td>
        </tr>
        <tr>
            <td align="center">Fire</td>
            <td align="center">Smoke</td>
            <td align="center">Fire</td>
            <td align="center">Smoke</td>
            <td align="center">Fire</td>
            <td align="center">Smoke</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">model9</td>
            <td align="center">yolov8s</td>
            <td align="center">200</td>
            <td align="center">28.4</td>
            <td align="center">640</td>
            <td align="center">1142</td>
            <td align="center">38</td>
            <td align="center">1 / 30</td>
            <td align="center">0.663</td>
            <td align="center">0.935</td>
            <td align="center">0.633</td>
            <td align="center">0.708</td>
            <td align="center">0.675</td>
            <td align="center">0.848</td>
        </tr>
        <tr>
            <td align="center">model10</td>
            <td align="center">yolov8n</td>
            <td align="center">200</td>
            <td align="center">8.1</td>
            <td align="center">800</td>
            <td align="center">1142</td>
            <td align="center">38</td>
            <td align="center">1 / 30</td>
            <td align="center">0.697</td>
            <td align="center">0.835</td>
            <td align="center">0.633</td>
            <td align="center">0.75</td>
            <td align="center">0.735</td>
            <td align="center">0.856</td>
        </tr>
    </tbody>
</table>

# Benchmarks
<table>
    <thead>
        <tr>
            <td rowspan=2 align="center">Format</td>
            <td colspan=2 align="center">Size(MB)</td>
            <td colspan=2 align="center">metrics / mAP50-90(B)</td>
            <td colspan=2 align="center">Inference time (ms/im)</td>
            <td colspan=2 align="center">FPS</td>
        </tr>
        <tr>
            <td align="center">model9</td>
            <td align="center">model10</td>
            <td align="center">model9</td>
            <td align="center">model10</td>
            <td align="center">model9</td>
            <td align="center">model10</td>
            <td align="center">model9</td>
            <td align="center">model10</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">torchscript</td>
            <td align="center">42.9</td>
            <td align="center">11.9</td>
            <td align="center">0.4253</td>
            <td align="center">0.4491</td>
            <td align="center">709.81</td>
            <td align="center">554.26</td>
            <td align="center">1.41</td>
            <td align="center">1.8</td>
        </tr>
        <tr>
            <td align="center">onnx</td>
            <td align="center">42.7</td>
            <td align="center">11.8</td>
            <td align="center">0.4253</td>
            <td align="center">0.4491</td>
            <td align="center">627.41</td>
            <td align="center">335.23</td>
            <td align="center">1.59</td>
            <td align="center">2.98</td>
        </tr>
        <tr>
            <td align="center">openvino</td>
            <td align="center">42.8</td>
            <td align="center">11.8</td>
            <td align="center">0.4253</td>
            <td align="center">0.4491</td>
            <td align="center">621.4</td>
            <td align="center">304.58</td>
            <td align="center">1.61</td>
            <td align="center">3.28</td>
        </tr>
        <tr>
            <td align="center">tflite</td>
            <td align="center">42.7</td>
            <td align="center">11.8</td>
            <td align="center">0.4253</td>
            <td align="center">0.4491</td>
            <td align="center">720.44</td>
            <td align="center">362.28</td>
            <td align="center">1.39</td>
            <td align="center">2.76</td>
        </tr>
        <tr>
            <td align="center">paddle</td>
            <td align="center">85.3</td>
            <td align="center">23.6</td>
            <td align="center">0.4253</td>
            <td align="center">0.4491</td>
            <td align="center">837.81</td>
            <td align="center">649.0</td>
            <td align="center">1.19</td>
            <td align="center">1.54</td>
        </tr>
        <tr>
            <td align="center">mnn</td>
            <td align="center">42.6</td>
            <td align="center">11.7</td>
            <td align="center">0.4253</td>
            <td align="center">0.4491</td>
            <td align="center">868.26</td>
            <td align="center">328.69</td>
            <td align="center">1.15</td>
            <td align="center">3.04</td>
        </tr>
        <tr>
            <td align="center">ncnn</td>
            <td align="center">42.6</td>
            <td align="center">11.7</td>
            <td align="center">0.4253</td>
            <td align="center">0.4491</td>
            <td align="center">728.85</td>
            <td align="center">379.68</td>
            <td align="center">1.37</td>
            <td align="center">2.63</td>
        </tr>
    </tbody>
</table>


# Test models
### Model 9 test video 1

https://github.com/user-attachments/assets/7b1a10f9-175b-4b31-9517-bf8201da17e5

### Model 10 test video 1

https://github.com/user-attachments/assets/db0a3830-c58e-4dfe-89c5-0b2546023344

### Model 9 test video 2

https://github.com/user-attachments/assets/45bb5d7e-f62b-46bd-9fd2-25327d750fb5

### Model 10 test video 2

https://github.com/user-attachments/assets/56d10118-7538-45ec-a9c3-95034020837f
