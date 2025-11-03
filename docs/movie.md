# 🎬 Modelo Movie: Documentação Oficial

Este documento descreve a estrutura do modelo `Movie` e seus relacionados, usado no app `movies`, com o objetivo de registrar filmes em um sistema profissional.

---

## 🧩 Estrutura Geral

O sistema é baseado em três modelos principais:

- `Movie`: representa um filme
- `Category`: representa uma categoria (gênero)
- `Actor`: representa um ator

Todos seguem o padrão **TimeStampedModel**, que inclui `created_at` e `updated_at`.

---

## 🔍 Detalhamento dos Modelos

### 1. `TimeStampedModel`

```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

> **Descrição:** Modelo abstrato herdado pelos demais para registrar a data de criação e última atualização.

---

### 2. `Category`

```python
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
```

- Representa uma categoria de filme (ex: Ação, Comédia, Drama)
- Nome é único e ordenado alfabeticamente

---

### 3. `Actor`

```python
class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
```

- Representa um ator
- Campo opcional `birth_date` permite uso futuro com filtragens ou listas cronológicas

---

### 4. `Movie`

```python
class Movie(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    release_year = models.IntegerField(validators=[...])
    photo = models.ImageField(upload_to="movies/photos/%Y/%m/", blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    categories = models.ManyToManyField(Category, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")
```

- **title:** Nome do filme
- **slug:** Gerado automaticamente do `title` para URLs amigáveis
- **release_year:** Validado entre 1888 e ano atual + 1
- **photo:** Suporta upload com organização por ano/mês
- **trailer_url:** Link opcional para trailer
- **rating:** Nota do filme (ex: 8.5)
- **categories:** Relacionamento com `Category`
- **actors:** Relacionamento com `Actor`

#### 📌 Métodos

```python
 def save(self, *args, **kwargs):
     if not self.slug:
         self.slug = slugify(self.title)
     super().save(*args, **kwargs)
```

> Gera `slug` automaticamente a partir do título.

```python
 def get_absolute_url(self):
     return reverse("movies:detail", kwargs={"slug": self.slug})
```

> Retorna a URL canônica da view `detail` do filme.

---

## ✅ Considerações de Boas Práticas

- Slugs evitam duplicidade e facilitam URLs amigáveis
- `ManyToManyField` em `actors` e `categories` segue normalização
- `ImageField` com `upload_to` personalizado organiza uploads
- `rating` com `DecimalField` evita erros de precisão de float
- Campos opcionais bem definidos com `blank=True`, `null=True`

---

## 🧪 Exemplo de Migração

```bash
poetry run python manage.py makemigrations movies
poetry run python manage.py migrate
```

---

## 📦 Futuras Extensões

- Adicionar suporte a diretores
- Indexar por popularidade
- Integração com API externa para metadados
- Registro em admin e viewsets DRF

---

> Documentação gerada automaticamente com base no padrão DevilLint™
