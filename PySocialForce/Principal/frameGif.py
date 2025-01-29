from PIL import Image
import os

def salvar_frames(gif_path, output_folder, num_imagens):
    # Abrir o GIF
    gif = Image.open(gif_path)

    # Criar pasta de saída se não existir
    os.makedirs(output_folder, exist_ok=True)

    # Contar os frames totais do GIF
    total_frames = gif.n_frames
    step = total_frames // num_imagens  # Dividir o total de frames pelo número de imagens desejado

    # Salvar os frames selecionados
    for i in range(num_imagens):
        frame_index = i * step
        gif.seek(frame_index)  # Ir para o frame correspondente
        frame = gif.copy()
        frame.save(os.path.join(output_folder, f"frame_{i + 1}.png"))
        print(f"Frame {frame_index} salvo como frame_{i + 1}.png")

    print(f"{num_imagens} frames salvos na pasta '{output_folder}'.")

# Exemplo de uso
gif_path = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\mapa_1_formatura\seed_7\mapa_seed_7.gif"  # Substitua pelo caminho do seu GIF
output_folder = "D:\Faculdade\TCC\Codigo\TCC\PySocialForce\Principal\\frameGifs\Mapa_1_formatura"  # Pasta onde as imagens serão salvas
num_imagens = 10  # Número de imagens desejado

salvar_frames(gif_path, output_folder, num_imagens)
