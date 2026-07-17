import os
from onnxruntime.quantization import quantize_dynamic, QuantType

def main() :
    # Import the baseline model after quantization export to new file
    input_model = os.path.abspath("models/baseline.onnx")
    output_model =os.path.abspath("models/quantized.onnx")

    print(f"Reading from : {input_model}")
    print(f"Exists : {os.path.exists(input_model)}")

    quantize_dynamic(
        model_input=input_model ,
        model_output=output_model ,
        weight_type=QuantType.QUInt8
        )
    # print where is model got saved
    print(f"Quantized model saved to {output_model}")

if __name__ == "__main__" :
    main()
