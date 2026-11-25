// Frequency count
const count = new Map();
for (const x of items) {
  count.set(x, (count.get(x) ?? 0) + 1);
}

// Grouping
const groups = new Map();
for (const item of items) {
  const key = 0/* what makes items belong together? */;
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key).push(item);
}