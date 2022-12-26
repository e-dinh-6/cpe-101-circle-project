pt = ray.pt
for t in range(1, 101):
    if dot_vector(vector_from_to(pt, sphere.center), vector_from_to(pt, sphere.center)) == sphere.radius ** 2:
        return pt
    pt = translate_point(pt, scale_vector(ray.dir, t))
return None

