import { useState, useEffect } from "react";

//? componente principal da aplicação SPA.
//* responsável por:
//* - cadastrar recursos
//* - listar recursos (com paginação)
//* - editar recursos
//* - excluir recursos
//* - integrar com Smart Assist (IA)

function App() {

    //? estados do formulário
    const [title, setTitle] = useState("");
    const [resourceType, setResourceType] = useState("PDF");
    const [description, setDescription] = useState("");
    const [url, setUrl] = useState("");
    const [tags, setTags] = useState([]);

    //? estados de controle da aplicação
    const [resources, setResources] = useState([]);
    const [page, setPage] = useState(1);
    const [loadingAI, setLoadingAI] = useState(false);
    const [editingId, setEditingId] = useState(null);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);

    //? função responsável por buscar os recursos da API, e executa sempre que a página muda (paginação)
    useEffect(() => {
        fetch(`http://localhost:8000/resources?page=${page}&limit=5`)
            .then(res => res.json())
            .then(data => setResources(data))
            .catch(() => setError("Erro ao carregar recursos."));
    }, [page]);

    //? função de geração automática de descrição com IA, envia título e tipo para o backend, backend consulta Gemini e retorna JSON estruturado
    const handleSmartAssist = async () => {
        try {
            setLoadingAI(true);
            setError(null);

            const response = await fetch(
                "http://localhost:8000/resources/smart-assist",
                {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        title,
                        resource_type: resourceType,
                    }),
                }
            );

            if (!response.ok) {
                throw new Error("AI request failed");
            }

            const data = await response.json();

            //? atualizando automaticamente os campos
            setDescription(data.description);
            setTags(data.tags);

        } catch (err) {
            setError("Erro ao gerar descrição com IA.");
        } finally {
            setLoadingAI(false);
        }
    };
    //? função de envio do formulário
    //? se estiver editando → faz PUT
    //? se não → faz POST
    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        setSuccess(null);

        try {
            const endpoint = editingId
                ? `http://localhost:8000/resources/${editingId}`
                : "http://localhost:8000/resources/";

            const method = editingId ? "PUT" : "POST";

            const response = await fetch(endpoint, {
                method,
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    title,
                    description,
                    resource_type: resourceType,
                    url,
                    tags,
                }),
            });

            if (!response.ok) {
                throw new Error("Failed request");
            }

            setSuccess(editingId ? "Recurso atualizado!" : "Recurso cadastrado!");

            //? resetando formulário
            setTitle("");
            setDescription("");
            setUrl("");
            setTags([]);
            setEditingId(null);

            //? recarregando lista
            fetch(`http://localhost:8000/resources?page=${page}&limit=5`)
                .then(res => res.json())
                .then(data => setResources(data));

        } catch (err) {
            setError("Erro ao salvar recurso.");
        }
    };

    //? função para excluir recurso
    const deleteResource = async (id) => {
        try {
            await fetch(`http://localhost:8000/resources/${id}`, {
                method: "DELETE",
            });

            setResources(resources.filter(r => r.id !== id));
        } catch {
            setError("Erro ao excluir recurso.");
        }
    };

    //? função para iniciar edição, e preenche o formulário com dados existentes
    const editResource = (resource) => {
        setTitle(resource.title);
        setDescription(resource.description);
        setUrl(resource.url);
        setResourceType(resource.resource_type);
        setTags(resource.tags || []);
        setEditingId(resource.id);
    };

    //? renderização
    return (
        <div style={{ padding: "40px", fontFamily: "Arial" }}>
            <h1>Hub Inteligente de Recursos Educacionais</h1>

            <form onSubmit={handleSubmit}>

                {/* título */}
                <label>Título:</label><br />
                <input
                    style={{ width: "100%", padding: "8px", marginBottom: "10px" }}
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                />

                {/* tipo */}
                <label>Tipo:</label><br />
                <select
                    style={{ width: "100%", padding: "8px", marginBottom: "10px" }}
                    value={resourceType}
                    onChange={(e) => setResourceType(e.target.value)}
                >
                    <option value="PDF">PDF</option>
                    <option value="VIDEO">VIDEO</option>
                    <option value="LINK">LINK</option>
                </select>

                {/* botão IA */}
                <button
                    type="button"
                    onClick={handleSmartAssist}
                    disabled={loadingAI || !title}
                    style={{ marginBottom: "20px", marginTop: "10px" }}
                >
                    {loadingAI ? "Gerando com IA..." : "Gerar Descrição com IA"}
                </button>

                {/* descrição */}
                <div>
                    <label>Descrição:</label><br />
                    <textarea
                        rows="6"
                        style={{ width: "100%", padding: "8px", marginBottom: "10px" }}
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        required
                    />
                </div>

                {/* URL */}
                <div>
                    <label>URL:</label><br />
                    <input
                        style={{ width: "100%", padding: "8px", marginBottom: "10px" }}
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                        required
                    />
                </div>

                {/* tags */}
                <div>
                    <label>Tags:</label><br />
                    <input
                        style={{ width: "100%", padding: "8px", marginBottom: "10px" }}
                        value={tags.join(", ")}
                        readOnly
                    />
                </div>

                <button type="submit">
                    {editingId ? "Atualizar Recurso" : "Cadastrar Recurso"}
                </button>

            </form>

            <hr style={{ margin: "40px 0" }} />

            <h2>Lista de Recursos</h2>

            {resources.map(resource => (
                <div key={resource.id} style={{ border: "1px solid #ccc", padding: "10px", marginBottom: "10px" }}>
                    <h3>{resource.title}</h3>
                    <p>{resource.description}</p>
                    <p><b>Tipo:</b> {resource.resource_type}</p>
                    <p><b>URL:</b> {resource.url}</p>
                    <p><b>Tags:</b> {resource.tags?.join(", ")}</p>

                    <button onClick={() => editResource(resource)}>Editar</button>
                    <button onClick={() => deleteResource(resource.id)} style={{ marginLeft: "10px" }}>
                        Excluir
                    </button>
                </div>
            ))}

            {/* paginação */}
            <div style={{ marginTop: "20px" }}>
                <button onClick={() => setPage(page - 1)} disabled={page === 1}>
                    Página Anterior
                </button>
                <span style={{ margin: "0 10px" }}>Página {page}</span>
                <button onClick={() => setPage(page + 1)}>
                    Próxima Página
                </button>
            </div>

            {/* Feedback */}
            {error && <p style={{ color: "red" }}>{error}</p>}
            {success && <p style={{ color: "green" }}>{success}</p>}
        </div>
    );
}

export default App;