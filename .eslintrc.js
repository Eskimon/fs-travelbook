module.exports = {
  extends: [
    // "plugin:vue/vue3-recommended",
    "plugin:vue/recommended",
  ],
  rules: {
    // override/add rules settings here, such as:
    // 'vue/no-unused-vars': 'error'
    "no-debugger": process.env.NODE_ENV === "development" ? "off" : "error",
    "no-console": "off",
    "comma-dangle": ["error", "always-multiline"],
    semi: [2, "never"],
    quotes: [2, "double"],
  },
  overrides: [
    {
      files: ["./**/*.vue"],
      // parser: require.resolve("vue-eslint-parser"),
      rules: {
        "vue/max-attributes-per-line": [
          "error",
          {
            singleline: 1,
            multiline: {
              max: 1,
              allowFirstLine: true,
            },
          },
        ],
      },
    },
  ],
}
